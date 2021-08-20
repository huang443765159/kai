import selectors
import socket
import threading


class UDP(object):

    def __init__(self, recv_callback, event_callback, error_callback, recv_length=32, port=10000):
        # SELECT
        self._select = selectors.DefaultSelector()
        # CALLBACK
        self._recv_callback = recv_callback
        self._event_callback = event_callback
        self._error_callback = error_callback
        # UDP
        self._udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self._is_bound = False
        self._recv_length = recv_length
        self._port = port
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            self._binding()
            events = self._select.select(timeout=1)
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)
            if not self._select.get_map():
                time.sleep(1)

    def _binding(self):
        if not self._is_bound:
            success = False
            self._udp.close()
            self._udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # SO_REUSEADDR
            self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # FOR BROADCAST
            self._udp.setblocking(False)
            host_addr = ('', self._port)  # FOR BROADCAST
            try:
                self._udp.bind(host_addr)
                self._select.register(self._udp, selectors.EVENT_READ, self._recv)
                success = True
            except socket.error as err:
                self._error_callback(module='UDP', code='BIND', value=err)
            if success != self._is_bound:
                self._is_bound = success
                self._event_callback(module='UDP', code='BIND', value=(self._is_bound, host_addr))
        return self._is_bound

    def _recv(self, conn, mask):
        rx_msg, addr = conn.recvfrom(self._recv_length)
        if rx_msg:
            self._recv_callback(protocol='UDP', rx_msg=rx_msg, ip=addr[0])
        else:
            pass

    def set_recv_length(self, length):
        self._recv_length = length

    def get_recv_length(self):
        return self._recv_length

    def _send(self, data, ip):
        success = False
        if self._is_bound:
            try:
                self._udp.sendto(data, (ip, self._port))
                success = True
            except socket.error as err:
                self._is_bound = False
                self._select.unregister(self._udp)
                self._error_callback(module='UDP', code='TX', value=err)
        return success

    def send_to(self, data, ip):
        return self._send(data, ip)

    def send_broadcast(self, data):
        return self._send(data, ip='<broadcast>')

    def is_bound(self):
        return self.is_bound


if __name__ == '__main__':

    import time

    def recv_cb(protocol, rx_msg, ip):
        print(f'{protocol} RX: {rx_msg} ({ip})')

    def event_cb(module, code, value):
        print(f'EVENT_RX: {module} {code} {value}')

    def error_cb(module, code, value):
        print(f'ERROR: {module} {code} {value}')

    udp = UDP(recv_cb, event_cb, error_cb, port=10000)

    while 1:
        udp.send_to(b'\xff\x00\x00\xaa', ip='192.168.50.104')
        udp.send_broadcast(b'\x88')
        time.sleep(1)
