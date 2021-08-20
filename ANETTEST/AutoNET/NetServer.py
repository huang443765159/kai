from ANETTEST.AutoNET.Socket.UDP import UDP
from ANETTEST.AutoNET.Socket.TcpServer import TcpServer
from ANETTEST.AutoNET.Inviter.InviterTX import InviterTX


class NetServer(object):

    def __init__(self, event_cb, error_cb, tcp_recv_cb, tcp_port, tcp_rx_len=256,
                 udp_recv_cb=None, udp_port=9999, launch_delay=0):
        # NETWORK
        self.udp = UDP(event_cb=event_cb, error_cb=error_cb, recv_cb=udp_recv_cb, port=udp_port,
                       launch_delay=launch_delay)
        self.tcp = TcpServer(event_cb=event_cb, error_cb=error_cb, recv_cb=tcp_recv_cb, port=tcp_port,
                             rx_length=tcp_rx_len, launch_delay=launch_delay)
        self._inviterTX = InviterTX(udp=self.udp, event_cb=event_cb, error_cb=error_cb)
        # COPY FUNC
        self.get_my_ip = self.tcp.get_my_ip
        self.get_server_port = self.tcp.get_server_port
        self.get_client_ips = self.tcp.get_client_ips

    # INVITER
    def set_device_token(self, device_token: str):
        if device_token != self._inviterTX.get_device_token():
            self.tcp.disconnect_all()
            self._inviterTX.set_device_token(device_token=device_token)

    def get_device_token(self):
        return self._inviterTX.get_device_token()

    def set_device_type(self, device_type: str):
        self._inviterTX.set_device_type(device_type=device_type)

    def get_device_type(self):
        return self._inviterTX.get_device_type()

    def set_device_id(self, device_id: int):
        self._inviterTX.set_device_id(device_id=device_id)

    def get_device_id(self):
        return self._inviterTX.get_device_id()

    def set_inviter_ena(self, ena: bool):
        self._inviterTX.set_enable(ena=ena)

    def get_inviter_ena(self):
        return self._inviterTX.get_enable()

    # SYSTEM
    def exit(self):
        self._inviterTX.exit()
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

    server = NetServer(event_cb=event_cb_, error_cb=error_cb_, tcp_recv_cb=tcp_recv_cb_, tcp_port=10000)
    server.set_device_token(device_token='KK')
    server.set_device_type(device_type='OK')
    server.set_device_id(device_id=8)
    server.set_inviter_ena(ena=True)
    while 1:
        time.sleep(1)
        server.tcp.send_broadcast(b'message from server')

