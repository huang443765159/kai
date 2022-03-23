import socket
import time


class Udp(object):

    def __init__(self, ip='192.168.50.170', port=54250):
        self._ip = ip
        self._port = port
        self._udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._working()

    def _recv(self):
        data = self._udp.recv(10)
        if data:
            print(data)
        else:
            print('RX err')

    def _working(self):
        while 1:
            try:
                self._udp.bind((self._ip, self._port))
            except socket.error:
                print('Connect err')
                time.sleep(1)
                continue
            # while 1:
            #     self._udp.sendto(b'hello Tom', (self._ip, self._port))
            #     self._recv()
            #     time.sleep(1)


if __name__ == '__main__':
    udp = Udp()
