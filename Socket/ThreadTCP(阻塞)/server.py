import selectors
import socket
import time
import threading


class TcpServer(object):

    def __init__(self, event_cb, err_cb, recv_cb, port):

        self._select = selectors.DefaultSelector()

        self._event_cb = event_cb
        self._err_cb = err_cb
        self._recv_cb = recv_cb

        self._port = port
        self._ip = None
        self._client = None
        self._bind = False
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._select.register(self._server, selectors.EVENT_READ, self._accept)

        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _accept(self, sock, mask):
        conn, addr = sock.accept()
        self._client = conn
        self._select.register(self._client, selectors.EVENT_READ, self._recv)

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
                    time.sleep(2)
                except socket.error as err:
                    self._event_cb(module='TCP', code='TX', value=err)

    def _tcp_lost(self):
        self._bind = False
        self._select.unregister(self._client)
        self._client.close()
        self._client = None
        self._event_cb(module='TCP', code='Bind', value=self._bind)

    def _recv(self, conn, mask):
        try:
            data = conn.recv(1024)
            if data == b'':
                self._tcp_lost()
            else:
                self._recv_cb(module='TCP', code='RX', value=data)
        except socket.error:
            self._tcp_lost()

    def set_tcp_ip(self, ip):
        self._ip = ip

    def get_tcp_ip(self):
        return self._ip

    def get_bind(self):
        return self._bind


if __name__ == '__main__':

    def event_cb_(module, code, value):
        print(f'{module} {code} {value}')

    def err_cb_(module, code, value):
        print(f'{module} {code} {value}')

    def recv_cb_(module, code, value):
        print(f'{module} {code} {value}')

    client = TcpServer(err_cb_, err_cb_, recv_cb_, port=8888)
    client.set_tcp_ip('127.0.0.1')

    while 1:
        time.sleep(1)