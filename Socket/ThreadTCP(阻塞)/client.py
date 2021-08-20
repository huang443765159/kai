import socket
import selectors
import threading
import time


class TcpClient(object):

    def __init__(self, event_cb, recv_cb, err_cb, port):
        self._select = selectors.DefaultSelector()

        self._event_cb = event_cb
        self._recv_cb = recv_cb
        self._err_cb = err_cb

        self._port = port
        self._ip = None
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._client.settimeout(1)
        self._connected = False

        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            if not self._connected:
                try:
                    self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self._client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    self._client.connect((self._ip, self._port))
                    self._connected = True
                except socket.error as err:
                    self._err_cb(module='TCP', code='Connect', value=err)
                    time.sleep(1)
                    continue
                self._select.register(self._client, selectors.EVENT_READ, self._recv)
                self._event_cb(module='TCP', code='Connect', value=(self._connected, self._ip, self._port))
            else:
                events = self._select.select(timeout=1)
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj, mask)
                if not self._select.get_map():
                    time.sleep(1)

    def _tcp_lost(self):
        self._connected = False
        self._select.unregister(self._client)
        self._client.close()
        self._event_cb(module='TCP', code='Connect', value=(self._connected, self._ip, self._port))

    def _recv(self, conn, mask):
        try:
            data = conn.recv(1024)
            if data == b'':
                self._tcp_lost()
            else:
                self._recv_cb(module='TCP', code='RX', value=data)
        except socket.error:
            self._tcp_lost()

    def send(self, data: bytes):
        if self._connected:
            try:
                self._client.send(data)
            except socket.error as err:
                self._err_cb(module='TCP', code='Connect', value=err)
                self._tcp_lost()

    def set_tcp_ip(self, ip):
        self._ip = ip

    def get_tcp_ip(self):
        return self._ip

    def _connect(self):
        return self._connected


if __name__ == '__main__':

    def event_cb_(module, code, value):
        print(f'{module} {code} {value}')

    def err_cb_(module, code, value):
        print(f'{module} {code} {value}')

    def recv_cb_(module, code, value):
        print(f'{module} {code} {value}')

    client = TcpClient(err_cb_, err_cb_, recv_cb_, port=1020)
    client.set_tcp_ip('127.0.0.1')

    while 1:
        time.sleep(1)
        client.send(b'\xb1\xb2')
        time.sleep(2)