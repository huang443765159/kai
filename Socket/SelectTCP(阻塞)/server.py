import socket
import selectors
import time


class Server(object):

    def __init__(self, ip='127.0.0.1', port=8888):

        self._ip = ip
        self._port = port
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._select = selectors.DefaultSelector()
        self._select.register(self._server, selectors.EVENT_READ, self._accept)
        self._bind = False
        self._client = None
        self._working()

    def _working(self):
        while 1:
            events = self._select.select(timeout=1)
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)
            if not self._select.get_map():
                time.sleep(1)

            if not self._bind:
                try:
                    self._server.bind((self._ip, self._port))
                    self._server.listen()
                    self._bind = True
                except socket.error as err:
                    pass

            if self._client is not None:
                try:
                    self._client.send(b'\xc1\xc2\xc3')
                except socket.error:
                    pass

    def _tcp_lost(self):
        self._bind = False
        self._select.unregister(self._client)
        self._client.close()
        self._client = None

    def _recv(self, conn, mask):
        try:
            data = conn.recv(1024)
            if data == b'':
                self._tcp_lost()
            else:
                print(data)
        except socket.error:
            self._tcp_lost()

    def _accept(self, sock, mask):
        conn, addr = sock.accept()
        print(addr)
        self._client = conn
        self._select.register(self._client, selectors.EVENT_READ, self._recv)


if __name__ == '__main__':
    server = Server()