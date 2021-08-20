from PyQt5.QtCore import QObject, pyqtSignal
from CarGuide.CARGUIDE.DRIVER.AutoNET.Socket.UDP import UDP


class NetInviter(object):

    def __init__(self, invite_type, device_id, event_cb=None, error_cb=None, udp_port=9999):
        self._event_cb = event_cb
        self._error_cb = error_cb
        self.udp = UDP(recv_cb=self._udp_recv, event_cb=self._event, error_cb=self._error,  port=udp_port)
        self.udp.set_invite_type(invite_type)
        self.udp.set_invite_id(device_id)

    def _udp_recv(self, rx_msg, ip):
        pass

    def _event(self, module, code, value):
        if self._event_cb:
            self._event_cb(module, code, value)

    def _error(self, module, code, value):
        if self._error_cb:
            self._error_cb(module, code, value)

    def set_invite_device(self, invite_type, device_id):
        self.udp.set_invite_type(invite_type)
        self.udp.set_invite_id(device_id)

    def get_invite_device(self):
        return self.udp.get_invite_type(), self.udp.get_invite_id()

    def set_invite_period(self, period):
        self.udp.set_invite_period(period)

    def get_invite_period(self):
        return self.udp.get_invite_period()

    def get_udp_port(self):
        return self.udp.get_port()


class QNetInviter(QObject):

    sign_sent_once = pyqtSignal(str, int)  # invite_type, invite_id
    sign_error = pyqtSignal(object, object, object)  # from anet_error

    def __init__(self, invite_type, device_id, udp_port=9999):
        super().__init__()
        self._inviter = NetInviter(invite_type, device_id, self._event, self._error, udp_port)

    def _event(self, module, code, value):
        if module == 'ANET_INVITER':
            if code == 'INVITE_SENT':
                invite_type, invite_id = value
                self.sign_sent_once.emit(invite_type, invite_id)

    def _error(self, module, code, value):
        self.sign_error.emit(module, code, value)

    def set_invite_device(self, invite_type, device_id):
        self._inviter.set_invite_device(invite_type, device_id)

    def get_invite_device(self):
        return self._inviter.get_invite_device()

    def set_invite_period(self, period):
        self._inviter.set_invite_period(period)

    def get_invite_period(self):
        return self._inviter.get_invite_period()

    def get_udp_port(self):
        return self._inviter.get_udp_port()
