import socket
import selectors
import time


class Client(object):

    def __init__(self, ip='127.0.0.1', port=8888):

        self._ip = ip
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._select = selectors.DefaultSelector()
        self._connect = False
        self._working()

    def _working(self):
        while 1:
            if not self._connect:
                try:
                    self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    self._socket.connect((self._ip, self._port))
                    self._connect = True
                except socket.error:
                    time.sleep(1)
                    continue
                self._select.register(self._socket, selectors.EVENT_READ, self._recv)
            else:
                events = self._select.select(timeout=1)
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj, mask)
                if not self._select.get_map():
                    time.sleep(1)
            if self._connect:
                try:
                    self._socket.send(b'\xb1\xb2')
                except socket.error:
                    self._tcp_lost(self._socket)

    def _recv(self, conn, mask):
        try:
            data = conn.recv(1024)
            if data == b'':
                self._tcp_lost(conn)
            else:
                print(data)
        except socket.error:
            self._tcp_lost(conn)

    def _tcp_lost(self, conn):
        self._connect = False
        self._select.unregister(conn)
        conn.close()

    def _set_ip(self, ip):
        self._ip = ip

    def _get_ip(self):
        return self._ip

    def _is_connect(self):
        return self._connect


if __name__ == '__main__':

    client = Client()