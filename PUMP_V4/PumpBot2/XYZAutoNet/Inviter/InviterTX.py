import time

INVITER_HEAD = b'\x99\x00'


class InviterTX(object):

    def __init__(self, udp, event_cb, error_cb):
        self._udp = udp
        self._udp.set_inviterTX(inviterTX=self)
        self._event_cb = event_cb
        self._error_cb = error_cb
        # ATTR
        self._ena = False
        self._device_type = None
        self._device_id = None
        self._device_token = None
        self._tx_period = 5
        self._tx_ts = 0

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

    # PERIOD
    def set_tx_period(self, period):
        self._tx_period = period

    def get_tx_period(self):
        return self._tx_period

    # ENABLE
    def set_enable(self, ena):
        self._ena = bool(ena)

    def get_enable(self):
        return self._ena

    # SHOT
    def send_inviter(self):
        if self._udp.is_bound() and self._ena and self._device_token and time.time() - self._tx_ts > self._tx_period:
            self._tx_ts = time.time()
            desc = f'{self._device_token}|{self._device_type}_{self._device_id}'
            self._udp.send_broadcast(data=INVITER_HEAD + desc.encode('UTF-8'))
            event_value = (self._device_token, self._device_type, self._device_id)
            self._event_cb(module='ANET_INVITER', code='INVITE_SENT', value=event_value)

    def exit(self):
        self._ena = False
