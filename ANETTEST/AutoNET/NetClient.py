from ANETTEST.AutoNET.Socket.UDP import UDP
from ANETTEST.AutoNET.Socket.TcpClient import TcpClient
from ANETTEST.AutoNET.Inviter.InviterRX import InviterRX


class NetClient(object):

    def __init__(self, event_cb, error_cb, tcp_recv_cb, tcp_port, tcp_rx_len=256,
                 udp_recv_cb=None, udp_port=9999, launch_delay=0):
        # CALLBACK
        self._udp_recv_cb = udp_recv_cb

        # NETWORK
        self.udp = UDP(recv_cb=self._udp_recv, event_cb=event_cb, error_cb=error_cb, port=udp_port,
                       launch_delay=launch_delay)
        self.tcp = TcpClient(recv_cb=tcp_recv_cb, event_cb=event_cb, error_cb=error_cb, port=tcp_port,
                             rx_length=tcp_rx_len, launch_delay=launch_delay)
        self._inviterRX = InviterRX(tcp_client=self.tcp, event_cb=event_cb)

        # COPY FUNC
        self.get_my_ip = self.tcp.get_my_ip
        self.get_server_ip = self.tcp.get_server_ip
        self.get_server_port = self.tcp.get_server_port

    def _udp_recv(self, rx_msg, ip):
        self._inviterRX.recv_inviter(rx_msg=rx_msg, ip=ip)
        if self._udp_recv_cb:
            self._udp_recv_cb(rx_msg, ip)

    # INVITER
    def set_device_token(self, device_token: str):
        if device_token != self._inviterRX.get_device_token():
            self.tcp.set_enable(ena=False)
            self._inviterRX.set_device_token(device_token=device_token)
            self.tcp.set_enable(ena=True)

    def get_device_token(self):
        return self._inviterRX.get_device_token()

    def set_device_type(self, device_type: str):
        self._inviterRX.set_device_type(device_type=device_type)

    def get_device_type(self):
        return self._inviterRX.get_device_type()

    def set_device_id(self, device_id: int):
        self._inviterRX.set_device_id(device_id=device_id)

    def get_device_id(self):
        return self._inviterRX.get_device_id()

    def set_inviter_ena(self, ena: bool):
        self._inviterRX.set_enable(ena=ena)

    def get_inviter_ena(self):
        return self._inviterRX.get_enable()

    # SYSTEM
    def exit(self):
        self._inviterRX.exit()
        self.tcp.exit()
        self.udp.exit()


if __name__ == '__main__':

    import time

    def tcp_recv_cb_(rx_msg, ip):
        print(f'TCP_RX: {rx_msg} ({ip})')

    def event_cb_(module, code, value):
        print(f'EVENT_RX: {module} {code} {value}')

    def error_cb_(module, code, value):
        print(f'ERROR: {module} {code} {value}')

    client = NetClient(tcp_recv_cb=tcp_recv_cb_, event_cb=event_cb_, error_cb=error_cb_, tcp_port=10000)
    client.set_device_type(device_type='OK')
    client.set_device_id(device_id=8)
    client.set_device_token(device_token='KK')
    client.set_inviter_ena(ena=True)
    while 1:
        time.sleep(1)
        client.tcp.send(b'message from client')
