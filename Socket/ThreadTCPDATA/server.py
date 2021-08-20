import socket
import selectors
import threading
import time
import struct
from Socket.ThreadTCPDATA._Tool import get_my_ip

MSG_HEAD = b'\xdd\xdd'


class TcpServer(object):

    def __init__(self, event_cb, error_cb, recv_cb, port):

        self._event_cb = event_cb
        self._error_cb = error_cb
        self._recv_cb = recv_cb

        self._select = None
        self._server = None
        self._client = dict()
        self._port = port
        self._ip = None
        self._bound = False

        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._select = selectors.DefaultSelector()
        self._select.register(self._server, selectors.EVENT_READ, self._accept)
        while 1:
            if self._bound:
                events = self._select.select(timeout=1)
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj, mask)

            else:
                ip = self._get_my_ip()
                if ip:
                    try:
                        self._server.bind((ip, self._port))
                        self._server.listen()
                        self._bound = True
                    except socket.error as err:
                        self._error_cb(module='TCP', code='BOUND', value=err)
                        time.sleep(1)
                    self._event_cb(module='TCP', code='BOUND', value=(self._bound, (ip, self._port)))

    def _tcp_lost(self, conn):
        if conn in self._select.get_map():
            self._select.unregister(conn)
        if conn in self._client:
            ip = self._client[conn]
            conn.close()
            self._client.pop(conn)
            self._event_cb(module='TCP', code='CONNECT', value=(False, (ip, self._port)))

    def _accept(self, sock, mask):
        conn, addr = sock.accept()
        ip, port = addr
        self._client[conn] = ip
        self._select.register(conn, selectors.EVENT_READ, self._recv)
        self._event_cb(module='TCP', code='CONNECT', value=(True, (ip, port)))

    def _recv(self, conn, mask):
        head = self._recv_length(conn, 4)
        if head:
            if head[:2] == MSG_HEAD:
                msg_len = struct.unpack('!H', head[2:4])[0]
                msg = self._recv_length(conn, msg_len)
                self._recv_cb(rx_msg=msg, ip=self._client[conn])

    def set_server_ip(self, ip):
        self._ip = ip

    def get_server_ip(self):
        return self._ip

    def get_server_port(self):
        return self._port

    def _recv_length(self, conn, length):
        data = None
        try:
            data = conn.recv(length)
            if data == b'':
                print('LOST b''')
                self._tcp_lost(conn)
        except socket.error as err:
            self._tcp_lost(conn)
        return data

    def send(self, conn, data: bytes):
        bytes_send = 0
        try:
            msg = MSG_HEAD + struct.pack('!H', len(data)) + data
            bytes_send = conn.send(msg)
            if bytes_send == 0:
                self._error_cb(module='TCP', code='TX BUF OVERFLOW', value=msg)
            bytes_send -= 4
        except socket.error as err:
            self._error_cb(module='TCP', code='TX', value=err)
            self._tcp_lost(conn)
        return bytes_send

    def send_to(self, data, ip):
        bytes_send = 0
        if ip in self._client.values():
            conn = list(self._client.keys())[list(self._client.values()).index(ip)]
            bytes_send = self.send(conn, data)
        return bytes_send

    def send_broad(self, data):
        ip = list()
        if self._client:
            for conn in list(self._client.keys()):
                bytes_send = self.send(conn, data)
                if bytes_send:
                    ip.append(self._client[conn])
        return ip

    def _get_my_ip(self):
        self._ip = get_my_ip()
        return self._ip


if __name__ == '__main__':
    import time


    def recv_cb_(rx_msg, ip):
        print(f'TCP_RX: {rx_msg} ({ip})')


    def event_cb_(module, code, value):
        print(f'EVENT_RX: {module} {code} {value}')


    def error_cb_(module, code, value):
        print(f'ERROR: {module} {code} {value}')


    SER_PORT = 10001

    server = TcpServer(event_cb=event_cb_, error_cb=error_cb_, recv_cb=recv_cb_, port=SER_PORT)
    while 1:
        time.sleep(2)
        server.send_broad(b'\x12\x11')