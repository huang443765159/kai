from CarGuide.CARGUIDE.DRIVER.AutoNET.Socket.UDP import UDP
from CarGuide.CARGUIDE.DRIVER.AutoNET.Socket.TcpClient import TcpClient


class NetClient(object):

    def __init__(self, event_cb, error_cb, tcp_recv_cb, tcp_port, invite_type, device_id,
                 udp_recv_cb=None, udp_port=9999):
        # CALLBACK
        self._udp_recv_cb = udp_recv_cb
        self._event_cb = event_cb
        self._error_cb = error_cb
        # UDP / TCP
        self.udp = UDP(recv_cb=self._udp_recv, event_cb=self._event_cb, error_cb=self._error_cb, port=udp_port)
        self.tcp = TcpClient(recv_cb=tcp_recv_cb, event_cb=self._event_cb, error_cb=self._error_cb,  port=tcp_port)
        # INVITE
        self._invite_type = invite_type
        self._device_id = device_id

    def _udp_recv(self, rx_msg, ip):
        if rx_msg[0] == 0x99:
            if not self.tcp.is_connected():
                server_ip, device_name = rx_msg[2:].decode('utf-8').split('|')
                if device_name == f'{self._invite_type}_{self._device_id}':
                    self.tcp.set_server_ip(ip=server_ip)
                    self._event_cb(module='ANET_INVITER', code='GET_INVITE', value=(server_ip, device_name))
        else:
            if self._udp_recv_cb:
                self._udp_recv_cb(rx_msg, ip)

    def get_device_type(self):
        return self._invite_type

    def get_device_id(self):
        return self._device_id

    def get_my_ip(self):
        return self.tcp.get_my_ip()

    def get_server_ip(self):
        return self.tcp.get_server_ip()

    def get_server_port(self):
        return self.tcp.get_server_port()

    def close(self):
        self.tcp.close()
        self.udp.close()


if __name__ == '__main__':

    import time

    def tcp_recv_cb_(rx_msg, ip):
        print(f'TCP_RX: {rx_msg} ({ip})')

    def event_cb_(module, code, value):
        print(f'EVENT_RX: {module} {code} {value}')

    def error_cb_(module, code, value):
        print(f'ERROR: {module} {code} {value}')

    client = NetClient(tcp_recv_cb=tcp_recv_cb_, event_cb=event_cb_, error_cb=error_cb_,
                       tcp_port=10000,
                       invite_type='ABC', device_id=9)
    while 1:
        time.sleep(1)
        client.tcp.send(b'I am Client')
