import socket
import selectors
import threading
import time
import struct
from Socket.ThreadTCPDATA._Tool import get_my_ip

MSG_HEAD = b'\xdd\xdd'


class TcpClient(object):
    def __init__(self, event_cb, recv_cb, error_cb, port):

        self._event_cb = event_cb
        self._recv_cb = recv_cb
        self._error_cb = error_cb

        self._select = None
        self._client = None
        self._server_ip = None
        self._connected = False
        self._port = port

        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._select = selectors.DefaultSelector()
        while 1:
            if self._connected:
                events = self._select.select(timeout=1)
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj, mask)
            else:
                if self._server_ip is None:
                    time.sleep(1)
                    continue
                try:
                    self._client.close()
                    self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self._client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    self._client.connect((self._server_ip, self._port))
                    self._connected = True
                except socket.error as err:
                    if err.__class__ != TypeError:
                        self._error_cb(module='TCP', code='CONNECT', value=err)
                    time.sleep(1)
                    continue
                self._select.register(self._client, selectors.EVENT_READ, self._recv)
                event_value = (self._connected, (self._server_ip, self._port))
                self._event_cb(module='TCP', code='CONNECT', value=event_value)

    def _recv_length(self, conn, length):
        data = None
        try:
            data = conn.recv(length)
            if data == b'':
                print('LOST b''')
                self._tcp_lost()
        except socket.error as err:
            self._error_cb(module='TCP', code='RX', value=err)
            self._tcp_lost()
        return data

    def _recv(self, conn, mask):
        head = self._recv_length(conn, 4)
        if head:
            if head[:2] == MSG_HEAD:
                msg_len = struct.unpack('!H', head[2:4])[0]
                msg = self._recv_length(conn, msg_len)
                self._recv_cb(rx_msg=msg, ip=self._server_ip)

    def _tcp_lost(self):
        self._connected = False
        if self._client in self._select.get_map():
            self._select.unregister(self._client)
        self._client.close()
        self._event_cb(module='TCP', code='CONNECT', value=(self._connected, (self._server_ip, self._port)))

    def _set_server_ip(self, ip):
        self._server_ip = ip

    def _get_server_ip(self):
        return self._server_ip

    def _get_port(self):
        return self._port

    def _get_connected(self):
        return self._connected

    def send(self, data: bytes):
        bytes_sent = 0
        if self._connected:
            try:
                msg = MSG_HEAD + struct.pack('!H', len(data)) + data
                bytes_sent = self._client.send(msg)
                #  发送长度 包头2 + 2 + data长度
                if bytes_sent == 0:
                    self._error_cb(module='TCP', code='TX_BUF_OVERFLOW', value=msg)
                bytes_sent -= 4
            except socket.error as err:
                self._error_cb(module='TCP', code='SEND', value=err)
                self._tcp_lost()
        return bytes_sent

    def get_my_ip(self):
        ip = get_my_ip()
        self._server_ip = ip


if __name__ == '__main__':

    def event_cb_(module, code, value):
        print(f'<EVENT> {module} {code} {value}')

    def error_cb_(module, code, value):
        print(f'<ERROR> {module} {code} {value}')

    def recv_cb_(rx_msg, ip):
        print(f'<RX> {rx_msg} {ip}')

    client = TcpClient(event_cb=event_cb_, error_cb=error_cb_, recv_cb=recv_cb_, port=10001)
    client.get_my_ip()

    while 1:
        time.sleep(1)
        client.send(b'\xb1\xb2\xb3\xb5\xb6')