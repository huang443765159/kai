import selectors
import socket
import struct
import threading
from QTimer任务流模块.DRIVER.AutoNET.Socket._Tool import get_my_ip

TCP_HEAD = b'\xaa\xdd\xbb\xcc'
TCP_END = b'\xee\xee'


class TcpServer(object):

    def __init__(self, recv_cb, event_cb, error_cb, port, recv_length=1024):
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
        self._recv_length = recv_length
        # Thread
        self._thread = threading.Thread(target=self._working)
        self._thread_interval = 2
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # SO_REUSEADDR, SO_REUSEPORT
        self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 3500000)
        self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 3500000)
        # print('<TCP_TX_BUF> =', self._tcp.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))
        # print('<TCP_RX_BUF> =', self._tcp.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF))
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

    def _recv(self, conn):
        data = bytes()
        try:
            rx_msg = conn.recv(self._recv_length)
            if rx_msg:
                data += rx_msg
                while 1:
                    msg_head = data[:4]
                    if msg_head == TCP_HEAD:
                        # BAD MSG
                        if len(data) < 8:
                            print('RECV LOST')
                            self._client_lost(conn)
                            break
                        msg_len = struct.unpack('I', data[4:8])[0]
                        # NORMAL MSG
                        if len(data) > msg_len + 8:
                            msg = data[8:msg_len + 8]
                            msg_end = data[msg_len + 8:msg_len + 10]
                            if msg_end == TCP_END:
                                self._recv_cb(rx_msg=msg, ip=self._clients[conn])
                        # JOINT MSG
                        if len(data) < msg_len + 8:
                            part_msg = conn.recv(msg_len + 8 - len(data))
                            new_msg = data[8:] + part_msg
                            part_msg_end = conn.recv(2)
                            if part_msg_end == TCP_END:
                                self._recv_cb(rx_msg=new_msg, ip=self._clients[conn])
                        # APART MSG
                        data = data[msg_len + 10:]
                        # EMPTY MSG
                        if data == b'':
                            break
        except (BlockingIOError, socket.timeout, OSError) as err:
            print('<LOST> BlockingIOError', err)
        except (ConnectionResetError, ConnectionAbortedError) as err:
            print('<LOST> ConnectionResetError', err)
            self._client_lost(conn)

    def _conn_send(self, conn, data: bytes):
        bytes_sent = 0
        try:
            msg = TCP_HEAD + struct.pack('I', len(data)) + data + TCP_END
            bytes_sent = conn.send(msg)
            if bytes_sent != len(msg):
                print('[ERROR], TCP_TX', f'{bytes_sent}/{len(msg)}', msg)
                self._error_cb(module='ANET_TCP', code='TX_BUF_OVERFLOW', value=msg)
            bytes_sent -= 10
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

    @staticmethod
    def get_my_ip():
        return get_my_ip()

    def get_server_port(self):
        return self._port

    def exit(self):
        self._tcp.close()


if __name__ == '__main__':

    import time

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
