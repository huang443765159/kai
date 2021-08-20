import selectors
import socket
import struct
import threading
import time
from python_opencv_handleRGB_vtk_display.DRIVER.AutoNET.Socket._Tool import get_my_ip

TCP_HEAD = b'\xdd\xdd'


class TcpClient(object):

    def __init__(self, recv_cb, event_cb, error_cb, port):
        # CALLBACK
        self._recv_cb = recv_cb
        self._event_cb = event_cb
        self._error_cb = error_cb
        # TCP
        self._select = None
        self._tcp = None
        self._is_connected = False
        self._server_ip = None
        self._server_port = port
        self._is_launched = True  # LAUNCH WHEN APP_START
        # Thread
        self._thread = threading.Thread(target=self._working)
        self._thread_interval = 1
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
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
                if self._is_launched is False or self._server_ip is None:
                    time.sleep(self._thread_interval)
                    continue
                # CONNECT
                try:
                    self._tcp.close()
                    self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 3500000)
                    self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 3500000)
                    # print('<TCP_TX_BUF> =', self._tcp.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))
                    # print('<TCP_RX_BUF> =', self._tcp.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF))
                    self._tcp.connect((self._server_ip, self._server_port))
                    self._is_connected = True
                except socket.error as err:
                    if err.__class__ != TypeError:
                        self._error_cb(module='ANET_TCP', code='CONNECT', value=err)
                    time.sleep(self._thread_interval)
                    continue
                # REGISTER
                self._select.register(self._tcp, selectors.EVENT_READ, self._recv)
                event_value = (self._is_connected, (self._server_ip, self._server_port))
                self._event_cb(module='ANET_TCP', code='CONNECT', value=event_value)

    def _recv_length(self, conn, length):
        data = bytes()
        while len(data) < length:
            try:
                msg = conn.recv(length - len(data))
                if msg:
                    data += msg
                else:
                    # print('<LOST> b''', self._server_ip)
                    self._server_lost()
                    break
            except (BlockingIOError, socket.timeout, OSError) as err:
                print('<LOST> BlockingIOError', err)
            except (ConnectionResetError, ConnectionAbortedError) as err:
                print('<LOST> ConnectionResetError', err)
                self._server_lost()
                break
        # if len(data) != length:
        #     print('[ERROR<1>] TCP_RX', f'{len(data)}/{length}', data)
        return data

    def _recv(self, conn):
        head = self._recv_length(conn, 4)
        if head:
            if head[:2] == TCP_HEAD:
                msg_len = struct.unpack('!H', head[2:4])[0]
                msg = self._recv_length(conn, msg_len)
                self._recv_cb(rx_msg=msg, ip=self._server_ip)
            # else:
            #     print('[ERROR<2>] TCP_RX', head)

    # SEND
    def send(self, data: bytes):
        bytes_sent = 0
        if self._is_connected:
            try:
                msg = TCP_HEAD + struct.pack('!H', len(data)) + data
                bytes_sent = self._tcp.send(msg)
                if bytes_sent != len(msg):
                    print('ERROR, TCP_TX', f'{bytes_sent}/{len(msg)}', msg)
                    self._error_cb(module='ANET_TCP', code='TX_BUF_OVERFLOW', value=msg)
                bytes_sent -= 4
            except (BlockingIOError, socket.timeout, OSError) as err:
                pass
            except (ConnectionResetError, ConnectionAbortedError) as err:
                self._error_cb(module='ANET_TCP', code='SEND', value=err)
                self._server_lost()
        return bytes_sent

    def _server_lost(self):
        self._is_connected = False
        if self._tcp in self._select.get_map():
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

    # GET ATTR
    def is_launch(self):
        return self._is_launched

    @staticmethod
    def get_my_ip():
        return get_my_ip()

    # LAUNCH / STOP
    def launch(self):
        self._is_launched = True

    def stop(self):
        self._is_launched = False
        self._server_lost()

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



