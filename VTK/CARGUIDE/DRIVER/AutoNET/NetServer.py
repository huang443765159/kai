from CARGUIDE.DRIVER.AutoNET.Socket.TcpServer import TcpServer


class NetServer(object):

    def __init__(self, event_cb, error_cb, tcp_recv_cb, tcp_port):
        # CALLBACK
        self._event_cb = event_cb
        self._error_cb = error_cb
        # TCP
        self.tcp = TcpServer(recv_cb=tcp_recv_cb, event_cb=self._event_cb,  error_cb=self._error_cb, port=tcp_port)
        # COPY FUNC
        self.is_bound = self.tcp.is_bound
        self.is_connected = self.tcp.is_connected
        self.get_my_ip = self.tcp.get_my_ip
        self.get_server_port = self.tcp.get_server_port
        self.get_client_ips = self.tcp.get_client_ips

    def exit(self):
        self.tcp.exit()


if __name__ == '__main__':

    import time
    from CARGUIDE.DRIVER.AutoNET.NetInviter import NetInviter

    def tcp_recv_cb_(rx_msg, ip):
        print(f'TCP_RX: {rx_msg} ({ip})')

    def event_cb_(module, code, value):
        print(f'EVENT_RX: {module} {code} {value}')

    def error_cb_(module, code, value):
        print(f'ERROR: {module} {code} {value}')

    inviter = NetInviter(invite_type='ABC', invite_id=9)
    server = NetServer(event_cb=event_cb_, error_cb=error_cb_, tcp_recv_cb=tcp_recv_cb_, tcp_port=10000)
    while 1:
        time.sleep(1)
        server.tcp.send_broadcast(b'message from server')

