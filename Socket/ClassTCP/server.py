import socket
import time


class Server(object):

    def __init__(self, ip='127.0.0.1', port=8888):

        self._ip = ip
        self._port = port
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.settimeout(0.1)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server.bind((self._ip, self._port))
        self._server.listen()
        self._server.setblocking(False)
        self._working()

    def _working(self):
        while 1:
            try:
                print('wait for client connect', end=' ')
                conn, addr = self._server.accept()
                print(conn.getpeername(), addr)
            except socket.error:
                print('no one')
                time.sleep(1)
                continue
            while 1:
                conn.settimeout(0.1)
                self.recv(conn)
                try:
                    conn.send(b'\xb1\xb2\xb3\xb4')
                except socket.error as error:
                    print('TX err', error)
                    conn.close()
                    break
                time.sleep(1)

    def recv(self, conn):
        try:
            data = conn.recv(10)
            if data == b'':
                print('空包')
            else:
                print(data)
        except socket.error:
            print('RX err')
            conn.close()


if __name__ == '__main__':
    server = Server()
