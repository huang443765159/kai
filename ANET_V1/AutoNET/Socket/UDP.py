import time
import socket
import threading
import selectors
from ANET_V1.AutoNET.Socket._Tool import get_my_ip, get_socket_buffer_size

RX_LEN = 1024


class UDP(object):

    def __init__(self, recv_cb, event_cb, error_cb, port=10000, launch_delay=0):
        # CALLBACK
        self._recv_cb = recv_cb
        self._event_cb = event_cb
        self._error_cb = error_cb
        # UDP
        self._select = None
        self._udp = None
        self._is_bound = False
        self._port = port
        self._inviterTX = None
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread_delay = launch_delay
        self._thread.start()

    def _working(self):
        time.sleep(self._thread_delay)
        self._udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self._select = selectors.DefaultSelector()
        while 1:
            if self._is_bound:
                # EVENTS
                events = self._select.select(timeout=5 if self._inviterTX is None else self._inviterTX.get_tx_period())
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj)
                # INVITER
                if self._inviterTX is not None:
                    self._inviterTX.send_inviter()
            else:
                # BIND
                self._udp.close()
                self._udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # SO_REUSEADDR SO_REUSEPORT
                self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # FOR BROADCAST
                self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, get_socket_buffer_size())
                self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, get_socket_buffer_size())
                host_addr = ('', self._port)  # BIND FOR BROADCAST
                try:
                    self._udp.bind(host_addr)
                    self._select.register(self._udp, selectors.EVENT_READ, self._recv)
                    self._is_bound = True
                except socket.error as err:
                    self._error_cb(module='ANET_UDP', code='BIND', value=err)
                    time.sleep(1)
                    continue
                self._event_cb(module='ANET_UDP', code='BIND', value=(self._is_bound, host_addr))

    def _recv(self, conn):
        rx_msg, addr = conn.recvfrom(RX_LEN)
        if rx_msg and self._recv_cb:
            self._recv_cb(rx_msg=rx_msg, ip=addr[0])

    # SEND
    def _send(self, data, ip):
        bytes_sent = 0
        if self._is_bound:
            try:
                bytes_sent = self._udp.sendto(data, (ip, self._port))
            except socket.error as err:
                self._is_bound = False
                self._select.unregister(self._udp)
                self._error_cb(module='ANET_UDP', code='TX', value=err)
        return bytes_sent

    def send_to(self, data, ip):
        return self._send(data, ip)

    def send_broadcast(self, data):
        return self._send(data, ip='<broadcast>')

    # FUNC
    def is_bound(self):
        return self.is_bound

    def get_port(self):
        return self._port

    @staticmethod
    def get_my_ip():
        return get_my_ip()

    def set_inviterTX(self, inviterTX):
        self._inviterTX = inviterTX

    def exit(self):
        self._udp.close()


if __name__ == '__main__':

    def recv_cb_(rx_msg, ip):
        print(f'UDP_RX: {rx_msg} ({ip})')

    def event_cb_(module, code, value):
        print(f'EVENT_RX: {module} {code} {value}')

    def error_cb_(module, code, value):
        print(f'ERROR: {module} {code} {value}')

    udp = UDP(recv_cb_, event_cb_, error_cb_, port=10000)
    udp.inviterTX.set_device_type('BOT')
    udp.inviterTX.set_device_id(8)
    udp.inviterTX.set_tx_period(3)
    udp.inviterTX.set_enable(ena=True)
    while 1:
        # udp.send_broadcast(b'message from UDP')
        time.sleep(1)
