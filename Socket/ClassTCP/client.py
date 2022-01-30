import socket
import time


class Client(object):

    def __init__(self, ip='192.168.50.51', port=8888):

        self._ip = ip
        self._port = port
        self._working()

    def _working(self):
        while 1:
            try:
                print('Connect', end=' ')
                self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self._client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self._client.connect((self._ip, self._port))
                self._client.setblocking(False)
                print('success')
            except socket.error:
                print('failed')
                time.sleep(1)
                continue
            self.recv()

    def recv(self):
        while 1:
            try:
                self._client.settimeout(0.1)
                data = self._client.recv(3)
                if data == b'':
                    print('空')
                    break
                else:
                    print(data)
            except socket.error:
                print('RX err')
            try:
                self._client.send(b'\xaa\xbb\xcc\xdd')
            except socket.error:
                print('TX err')
                self._client.close()
                break
            time.sleep(1)


if __name__ == '__main__':
    client = Client()
