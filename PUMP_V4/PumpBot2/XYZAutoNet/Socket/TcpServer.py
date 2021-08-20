import time
import socket
import threading
import selectors
from ._decode import cut_message_by_head, get_data_len, decode_message
from ._decode import LEN_TOTAL, build_tx_message
from ..Tool import get_my_ip, get_socket_buffer_size


class TcpServer(object):

    def __init__(self, recv_cb, event_cb, error_cb, port, rx_length=256, launch_delay=0):
        # CALLBACK
        self._recv_cb = recv_cb
        self._event_cb = event_cb
        self._error_cb = error_cb
        # TCP
        self._select = None
        self._tcp = None
        self._is_bound = False
        self._port = port
        self._clients = dict()  # {socket_conn: '10.10.10.10'}
        self._rx_length = rx_length
        self._rx_buffer = bytes()
        # Thread
        self._thread = threading.Thread(target=self._working)
        self._thread_interval = 2
        self._thread.daemon = True
        self._thread_delay = launch_delay
        self._thread.start()

    def _working(self):
        time.sleep(self._thread_delay)
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # SO_REUSEADDR, SO_REUSEPORT
        self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, get_socket_buffer_size())
        self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, get_socket_buffer_size())
        self._select = selectors.DefaultSelector()
        self._select.register(self._tcp, selectors.EVENT_READ, self._accept)
        while 1:
            if self._is_bound:
                events = self._select.select(timeout=self._thread_interval)
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj)
            else:
                host_ip = self.get_my_ip()
                if host_ip:
                    try:
                        self._tcp.bind((host_ip, self._port))
                        self._tcp.listen()
                        self._is_bound = True
                    except socket.error as err:
                        self._error_cb(module='ANET_TCP', code='BIND', value=err)
                        time.sleep(self._thread_interval)
                    self._event_cb(module='ANET_TCP', code='BIND', value=(self._is_bound, (host_ip, self._port)))
                else:
                    print('[ERROR] ANET_SERVER: Network is unreachable')

    def _recv_length(self, conn, rx_length):
        rx_msg = bytes()
        try:
            msg = conn.recv(rx_length)
            if msg:
                rx_msg += msg
            else:
                self._client_lost(conn=conn)
        except (BlockingIOError, socket.timeout, OSError) as err:
            print('<LOST> BlockingIOError', err)
        except (ConnectionResetError, ConnectionAbortedError) as err:
            print('<LOST> ConnectionResetError', err)
            self._client_lost(conn=conn)
        return rx_msg

    def _recv(self, conn):
        # RX ONE MESSAGE
        self._rx_buffer += self._recv_length(conn=conn, rx_length=self._rx_length)
        while self._rx_buffer:
            # CUT_TO_HEAD
            msg_with_head = cut_message_by_head(buffer=self._rx_buffer)
            if not msg_with_head:
                break
            # GET_DATA_LEN
            data_len, miss_len = get_data_len(msg_with_head=msg_with_head)
            if miss_len > 0:  # MISS_DATA
                new_buffer = self._recv_length(conn=conn, rx_length=miss_len)
                if new_buffer:
                    self._rx_buffer += new_buffer
                else:
                    break
            else:  # PARSE_DATA
                data, self._rx_buffer, error = decode_message(msg_with_head=msg_with_head, data_len=data_len)
                if data:
                    self._recv_cb(rx_msg=data, ip=self._clients[conn])
                if error:
                    self._error_cb(module='ANET_TCP', code=error, value=self._rx_buffer)

    def _conn_send(self, conn, data: bytes):
        bytes_sent = 0
        try:
            msg, msg_len = build_tx_message(data=data)
            bytes_sent = conn.send(msg)
            if bytes_sent != msg_len:
                print('[ERROR], TCP_TX', f'{bytes_sent}/{len(msg)}', msg)
                self._error_cb(module='ANET_TCP', code='TX_BUF_OVERFLOW', value=msg)
            bytes_sent -= LEN_TOTAL
        except (BlockingIOError, socket.timeout, OSError) as err:
            pass
        except (ConnectionResetError, ConnectionAbortedError) as err:
            self._error_cb(module='ANET_TCP', code='SEND', value=err)
            self._client_lost(conn)
        return bytes_sent

    # SEND
    def send_to(self, data, ip):
        bytes_sent = 0
        if ip in self._clients.values():
            conn = list(self._clients.keys())[list(self._clients.values()).index(ip)]
            bytes_sent = self._conn_send(conn, data)
        return bytes_sent

    def send_broadcast(self, data):
        arrived_clients_ip = list()
        if self._clients:
            for conn in list(self._clients.keys()):
                bytes_sent = self._conn_send(conn, data)
                if bytes_sent:
                    arrived_clients_ip.append(self._clients[conn])
        return arrived_clients_ip

    # ACCEPT / LOST
    def _accept(self, sock):
        conn, addr = sock.accept()
        ip, port = addr
        self._clients[conn] = ip
        self._select.register(conn, selectors.EVENT_READ, self._recv)
        self._event_cb(module='ANET_TCP', code='CONNECT', value=(True, (ip, self._port)))

    def _client_lost(self, conn):
        if conn in self._select.get_map():
            self._select.unregister(conn)
        if conn in self._clients:
            ip = self._clients[conn]
            conn.close()
            self._clients.pop(conn)
            self._event_cb(module='ANET_TCP', code='CONNECT', value=(False, (ip, self._port)))

    # FUNC
    def is_bound(self):
        return self.is_bound

    def get_client_ips(self):
        return list(self._clients.values())

    def is_connected(self):
        return True if list(self._clients.values()) else False

    def disconnect_all(self):
        for conn in list(self._clients.keys()):
            self._client_lost(conn=conn)

    @staticmethod
    def get_my_ip():
        return get_my_ip()

    def get_server_port(self):
        return self._port

    def exit(self):
        self._tcp.close()


if __name__ == '__main__':

    def recv_cb_(rx_msg, ip):
        print(f'TCP_RX: {rx_msg} ({ip})')

    def event_cb_(module, code, value):
        print(f'EVENT_RX: {module} {code} {value}')

    def error_cb_(module, code, value):
        print(f'ERROR: {module} {code} {value}')

    SER_PORT = 10001

    server = TcpServer(recv_cb_, event_cb_, error_cb_, port=SER_PORT)
    print('MY_IP=', server.get_my_ip())
    while 1:
        time.sleep(2)
        server.send_broadcast(b'message from server')
