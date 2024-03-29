import selectors
import socket
import threading
import time
from CARGUIDE.DRIVER.AutoNET.Socket._Tool import get_my_ip

RX_LEN = 1024


class UDP(object):

    def __init__(self, recv_cb, event_cb, error_cb, port=10000):
        # CALLBACK
        self._recv_cb = recv_cb
        self._event_cb = event_cb
        self._error_cb = error_cb
        # UDP
        self._select = None
        self._udp = None
        self._is_bound = False
        self._port = port
        # INVITE
        self._invite_type = None
        self._invite_id = None
        self._invite_period = 5
        self._invite_ts = 0
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        self._udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self._select = selectors.DefaultSelector()
        while 1:
            if self._is_bound:
                # EVENTS
                events = self._select.select(timeout=self._invite_period)
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj)
                # INVITER
                if self._is_bound and self._invite_type is not None and self._invite_period:
                    if time.time() - self._invite_ts > self._invite_period:
                        invite_info = b'\x99\x00'
                        my_ip = self.get_my_ip()
                        if my_ip:
                            desc = f'{my_ip}|{self._invite_type}_{self._invite_id}'
                            invite_info += desc.encode('UTF-8')
                            self.send_broadcast(data=invite_info)
                            self._invite_ts = time.time()
                            self._event_cb(module='ANET_INVITER', code='INVITE_SENT',
                                           value=(self._invite_type, self._invite_id, my_ip))
                        else:
                            print('[ERROR] ANET_UDP: Network is unreachable')
            else:
                # BIND
                self._udp.close()
                self._udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # SO_REUSEADDR SO_REUSEPORT
                self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # FOR BROADCAST
                # self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4194304)
                # self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4194304)
                # print('<UDP_TX_BUF> =', self._udp.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))
                # print('<UDP_RX_BUF> =', self._udp.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF))
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
        if rx_msg:
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

    def exit(self):
        self._udp.close()

    # INVITE
    def set_invite_type(self, invite_type):
        self._invite_type = invite_type

    def set_invite_id(self, invite_id):
        self._invite_id = invite_id

    def set_invite_period(self, period):
        self._invite_period = period

    def get_invite_type(self):
        return self._invite_type

    def get_invite_id(self):
        return self._invite_id

    def get_invite_period(self):
        return self._invite_period


if __name__ == '__main__':

    def recv_cb_(rx_msg, ip):
        print(f'UDP_RX: {rx_msg} ({ip})')

    def event_cb_(module, code, value):
        print(f'EVENT_RX: {module} {code} {value}')

    def error_cb_(module, code, value):
        print(f'ERROR: {module} {code} {value}')

    udp = UDP(recv_cb_, event_cb_, error_cb_, port=10000)
    udp.set_invite_type('BOT')
    udp.set_invite_id(8)
    udp.set_invite_period(3)  # means stop inviter
    while 1:
        udp.send_broadcast(b'message from UDP')
        time.sleep(1)
