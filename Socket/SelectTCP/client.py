import socket
import selectors
import time


class Client(object):

    def __init__(self, ip='0.0.0.0', port=8888):

        self._select = selectors.DefaultSelector()  # 默认
        self._ip = ip
        self._port = port
        self._client = None
        self._connected = False
        self._working()

    def _tcp_lost(self, conn):
        self._connected = False
        self._select.unregister(conn)
        conn.close()

    def _working(self):
        while 1:
            if not self._connected:
                try:
                    print('connect', end=' ')
                    self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self._client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    self._client.connect((self._ip, self._port))
                    self._client.setblocking(False)
                    self._connected = True
                    print('success')
                except socket.error:
                    print('failed')
                    time.sleep(1)
                    continue
                self._select.register(self._client, selectors.EVENT_READ, self._recv)
            else:
                events = self._select.select(timeout=1)
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj, mask)

                if self._connected:
                    try:
                        self._client.send(b'\xb1\xb2\xb3\xb4')
                    except socket.error:
                        print('TX err')
                        self._tcp_lost(self._client)
            time.sleep(1)

    def _recv(self, conn, mask):
        try:
            data = conn.recv(3)
            if data:
                print(data)
            else:
                self._tcp_lost(conn)
        except socket.error:
            self._tcp_lost(conn)


if __name__ == '__main__':
    client = Client()
