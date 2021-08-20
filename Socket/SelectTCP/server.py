import socket
import selectors
import time


class Server(object):

    def __init__(self, ip='192.168.50.62', port=50037, udp_port=4444, udp_ip='<broadcast>'):

        self._select = selectors.DefaultSelector()
        self._ip = ip
        self._port = port
        self._client = None
        self._bound = False
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._select.register(self._server, selectors.EVENT_READ, self._accept)
        self._tx_num = 0
        self._rx_num = 0
        # UDP
        self._udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self._upd_port = udp_port
        self._udp_ip = udp_ip
        #  要被回调的对象，事件（一般都是读），回调对象要给的函数
        self._working()

    def _tcp_lost(self):
        self._select.unregister(self._client)
        self._client.close()
        self._client = None
        print('Client disconnected')

    def _working(self):
        while 1:
            self._udp.sendto('Client broadcast message!'.encode('utf-8'), (self._udp_ip, self._upd_port))
            events = self._select.select(timeout=1)
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)
            if not self._bound:
                try:
                    print('TCP binding', end=' ')
                    self._server.bind((self._ip, self._port))
                    self._server.listen()
                    self._server.setblocking(False)
                    self._bound = True
                    print('success')
                except socket.error:
                    print('failed')
            if self._client is not None:
                try:
                    self._client.send(b'\xe1\xe2\xe3\xe4')
                    self._tx_num += 1
                    if self._tx_num == 10000:
                        self._client.close()
                except socket.error:
                    self._tcp_lost()
                    print('TX err')
            time.sleep(1)

    def _recv(self, conn, mask):
        try:
            data = conn.recv(5)
            if data:
                self._rx_num += 1
                print(data[0], self._rx_num)
            else:
                print('RX err')
                self._tcp_lost()
        except socket.error:
            self._tcp_lost()

    def _accept(self, sock, mask):
        conn, addr = sock.accept()
        # conn 是对方client, addr 是对方ip
        ip = addr[0]
        print('Incoming', ip)
        self._client = conn
        self._select.register(self._client, selectors.EVENT_READ, self._recv)


if __name__ == '__main__':

    server = Server()
