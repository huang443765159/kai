import socket
import selectors
import time


class Udp(object):

    def __init__(self, ip='127.0.0.1', port=8888):
        self._select = selectors.DefaultSelector()

        self._ip = ip
        self._port = port
        self._connect = False
        self._udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._select.register(self._udp, selectors.EVENT_READ, self._recv)

        self._working()

    def _recv(self, conn, mask):
        data = conn.recv(10)
        if data:
            print(data)
        else:
            print('RX err')
            self._connect = False

    def _working(self):
        while 1:
            if not self._connect:
                try:
                    print('binding...', end=' ')
                    self._udp.bind((self._ip, self._port))
                    print('success')
                    self._connect = True
                except socket.error:
                    print('failed')
                    time.sleep(1)
                    continue
            else:
                events = self._select.select(timeout=1)
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj, mask)
                if not self._select.get_map():
                    time.sleep(2)
                self._udp.sendto(b'hello Tom', (self._ip, self._port))
                time.sleep(1)


if __name__ == '__main__':

    udp = Udp()