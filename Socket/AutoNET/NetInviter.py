from PyQt5.QtCore import QObject, pyqtSignal
from python_opencv_handleRGB_vtk_display.DRIVER.AutoNET.Socket.UDP import UDP


class NetInviter(object):

    def __init__(self, invite_type, invite_id, event_cb=None, error_cb=None, udp_port=9999):
        self._event_cb = event_cb
        self._error_cb = error_cb
        self.udp = UDP(recv_cb=self._udp_recv, event_cb=self._event, error_cb=self._error,  port=udp_port)
        self.udp.set_invite_type(invite_type)
        self.udp.set_invite_id(invite_id)
        # COPY FUNC
        self.set_invite_type = self.udp.set_invite_type
        self.get_invite_type = self.udp.get_invite_type
        self.set_invite_id = self.udp.set_invite_id
        self.get_invite_id = self.udp.get_invite_id
        self.get_udp_port = self.udp.get_port
        self.get_my_ip = self.udp.get_my_ip
        self.exit = self.udp.exit
        # PERIOD [UDP_PERIOD==0 means STOP, LAUNCH WHEN APP_START]
        self._period = 5
        self.set_invite_period(self._period)

    def _udp_recv(self, rx_msg, ip):
        pass

    def _event(self, module, code, value):
        if self._event_cb:
            self._event_cb(module, code, value)

    def _error(self, module, code, value):
        if self._error_cb:
            self._error_cb(module, code, value)

    # INVITER PERIOD
    def set_invite_period(self, period):
        if period > 0:
            self._period = period
            self.udp.set_invite_period(period)

    def get_invite_period(self):
        return self._period

    # LAUNCH/STOP
    def is_launched(self):
        return bool(self.udp.get_invite_period())

    def launch(self):
        self.udp.set_invite_period(self._period)

    def stop(self):
        self.udp.set_invite_period(0)


class QNetInviter(QObject):

    sign_sent_once = pyqtSignal(str, int, str)  # invite_type, invite_id, my_ip
    sign_error = pyqtSignal(object, object, object)  # from anet_error

    def __init__(self, invite_type, invite_id, udp_port=9999):
        super().__init__()
        self._inviter = NetInviter(invite_type, invite_id, self._event, self._error, udp_port)
        # FUNC COPY
        self.set_invite_type = self._inviter.set_invite_type
        self.get_invite_type = self._inviter.get_invite_type
        self.set_invite_id = self._inviter.set_invite_id
        self.get_invite_id = self._inviter.get_invite_id
        self.set_invite_period = self._inviter.set_invite_period
        self.get_invite_period = self._inviter.get_invite_period
        self.get_udp_port = self._inviter.get_udp_port
        self.get_my_ip = self._inviter.get_my_ip
        self.is_launched = self._inviter.is_launched
        self.launch = self._inviter.launch
        self.stop = self._inviter.stop

    def _event(self, module, code, value):
        if module == 'ANET_INVITER':
            if code == 'INVITE_SENT':
                invite_type, invite_id = value
                self.sign_sent_once.emit(invite_type, invite_id, self._inviter.get_my_ip())

    def _error(self, module, code, value):
        self.sign_error.emit(module, code, value)

    def exit(self):
        self._inviter.exit()
