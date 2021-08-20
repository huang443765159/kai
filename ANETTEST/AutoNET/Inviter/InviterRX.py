INVITER_HEAD = b'\x99\x00'


class InviterRX(object):

    def __init__(self, tcp_client, event_cb):
        self._tcp_client = tcp_client
        self._event_cb = event_cb
        # ATTR
        self._ena = False
        self._device_type = None
        self._device_id = None
        self._device_token = None

    # DEVICE
    def set_device_type(self, device_type):
        self._device_type = device_type

    def set_device_id(self, device_id):
        self._device_id = device_id

    def set_device_token(self, device_token):
        self._device_token = device_token

    def get_device_type(self):
        return self._device_type

    def get_device_id(self):
        return self._device_id

    def get_device_token(self):
        return self._device_token

    # ENABLE
    def set_enable(self, ena):
        self._ena = bool(ena)

    def get_enable(self):
        return self._ena

    # INVITER
    def recv_inviter(self, rx_msg, ip):
        if self._ena:
            if rx_msg[:2] == INVITER_HEAD and not self._tcp_client.is_connected() and self._device_token:
                device_token, device_name = rx_msg[2:].decode('utf-8').split('|')
                if device_token == self._device_token and device_name == f'{self._device_type}_{self._device_id}':
                    self._tcp_client.set_server_ip(ip=ip)
                    self._event_cb(module='ANET_INVITER', code='GET_INVITE', value=(device_token, ip, device_name))

    def exit(self):
        self._ena = False
