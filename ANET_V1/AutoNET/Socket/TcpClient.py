import time
import socket
import threading
import selectors
from ANET_V1.AutoNET.Socket._Tool import get_my_ip, get_socket_buffer_size
from ANET_V1.AutoNET.Socket._decode import cut_message_by_head, get_data_len, decode_message
from ANET_V1.AutoNET.Socket._decode import LEN_TOTAL, build_tx_message


class TcpClient(object):

    def __init__(self, recv_cb, event_cb, error_cb, port, rx_length=256, launch_delay=0):
        # CALLBACK
        self._recv_cb = recv_cb
        self._event_cb = event_cb
        self._error_cb = error_cb
        # TCP
        self._ena = True
        self._select = None
        self._tcp = None
        self._ts_connected = 0
        self._is_connected = False
        self._server_ip = None
        self._server_port = port
        self._rx_buffer = bytes()
        self._rx_length = rx_length
        # Thread
        self._thread = threading.Thread(target=self._working)
        self._thread_interval = 1
        self._thread.daemon = True
        self._thread_delay = launch_delay
        self._thread.start()

    def _working(self):
        time.sleep(self._thread_delay)
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._select = selectors.DefaultSelector()
        while 1:
            if self._is_connected:
                # EVENTS CHECK
                events = self._select.select(timeout=self._thread_interval)
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj)
            else:
                # NOTHING TO DO
                if self._ena is False or self._server_ip is None:
                    time.sleep(self._thread_interval)
                    continue
                # CONNECT
                if time.time() - self._ts_connected > self._thread_interval:
                    self._ts_connected = time.time()
                    try:
                        self._tcp.close()
                        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, get_socket_buffer_size())
                        self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, get_socket_buffer_size())
                        self._tcp.connect((self._server_ip, self._server_port))
                    except socket.error as err:
                        if err.__class__ != TypeError:
                            self._error_cb(module='ANET_TCP', code='CONNECT', value=err)
                        continue
                    # REGISTER
                    self._is_connected = False
                    if self._tcp.fileno() != -1:
                        self._is_connected = True
                        self._select.register(self._tcp, selectors.EVENT_READ, self._recv)
                    event_value = (self._is_connected, (self._server_ip, self._server_port))
                    self._event_cb(module='ANET_TCP', code='CONNECT', value=event_value)

    def _recv_length(self, conn, rx_length):
        rx_msg = bytes()
        try:
            msg = conn.recv(rx_length)
            if msg:
                rx_msg += msg
            else:
                self._server_lost()
        except (BlockingIOError, socket.timeout, OSError) as err:
            print('<LOST> BlockingIOError', err)
        except (ConnectionResetError, ConnectionAbortedError) as err:
            print('<LOST> ConnectionResetError', err)
            self._server_lost()
        return rx_msg

    def _recv(self, conn):
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
                    self._recv_cb(rx_msg=data, ip=self._server_ip)
                if error:
                    self._error_cb(module='ANET_TCP', code=error, value=self._rx_buffer)

    # SEND
    def send(self, data: bytes):
        bytes_sent = 0
        if self._is_connected:
            try:
                msg, msg_len = build_tx_message(data=data)
                bytes_sent = self._tcp.send(msg)
                if bytes_sent != msg_len:
                    print('ERROR, TCP_TX', f'{bytes_sent}/{len(msg)}', msg)
                    self._error_cb(module='ANET_TCP', code='TX_BUF_OVERFLOW', value=msg)
                bytes_sent -= LEN_TOTAL
            except (BlockingIOError, socket.timeout, OSError) as err:
                pass
            except (ConnectionResetError, ConnectionAbortedError) as err:
                self._error_cb(module='ANET_TCP', code='SEND', value=err)
                self._server_lost()
        return bytes_sent

    def send_direct(self, msg):
        bytes_sent = 0
        if self._is_connected:
            try:
                bytes_sent = self._tcp.send(msg)
                if bytes_sent != len(msg):
                    print('ERROR, TCP_TX', f'{bytes_sent}/{len(msg)}', msg)
                    self._error_cb(module='ANET_TCP', code='TX_BUF_OVERFLOW', value=msg)
                bytes_sent -= LEN_TOTAL
            except (BlockingIOError, socket.timeout, OSError) as err:
                pass
            except (ConnectionResetError, ConnectionAbortedError) as err:
                self._error_cb(module='ANET_TCP', code='SEND', value=err)
                self._server_lost()
        return bytes_sent

    def _server_lost(self):
        self._is_connected = False
        # print(f'[debug] tcp={self._tcp}, map={self._select.get_map()}')
        if self._select is not None and self._tcp.fileno() != -1 and self._tcp in self._select.get_map():
            self._select.unregister(self._tcp)
        self._tcp.close()
        self._event_cb(module='ANET_TCP', code='CONNECT', value=(False, (self._server_ip, self._server_port)))

    # CONNECTION
    def set_server_ip(self, ip):
        self._server_ip = ip

    def get_server_ip(self):
        return self._server_ip

    def get_server_port(self):
        return self._server_port

    def is_connected(self):
        return self._is_connected

    # ENABLE
    def set_enable(self, ena):
        self._ena = bool(ena)
        if self._ena is False and self._tcp is not None:
            self._server_ip = None
            self._server_lost()

    def get_enable(self):
        return self._ena

    @staticmethod
    def get_my_ip():
        return get_my_ip()

    def exit(self):
        self._tcp.close()


if __name__ == '__main__':

    def recv_cb_(rx_msg, ip):
        print(f'<TCP_RX>  {rx_msg} ({ip})')

    def event_cb_(module, code, value):
        print(f'<EVENT>  {module} {code} {value}')

    def error_cb_(module, code, value):
        print(f'<ERROR>  {module} {code} {value}')

    SER_PORT = 10001

    client = TcpClient(recv_cb_, event_cb_, error_cb_, port=SER_PORT)
    client.set_server_ip(ip=client.get_my_ip())
    while 1:
        time.sleep(1)
        client.send(data=b'message from client')



