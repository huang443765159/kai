import struct
from PyQt5.QtCore import QObject, pyqtSignal
from LEDDISPLAY.DRIVE.AutoNET.NetClient import NetClient

TCP_PORT = 20010
LED_DISPLAY = {'WELCOME': 0x01, 'FORWARD': 0x02, 'STOP': 0x03, 'BACK': 0x04, 'WASH START': 0x05, 'WASH END': 0x06}


class LedDisplay(QObject):

    sign_display = pyqtSignal(str, bool)  # show, is_display
    sign_connection = pyqtSignal(bool, str, int)  # is_connected, ip, port
    sign_error = pyqtSignal(str, str, object)  # error_type, code, error

    def __init__(self):
        super().__init__()
        # NETWORK
        self._network = NetClient(event_cb=self._event, error_cb=self._error, tcp_recv_cb=self._recv,
                                  tcp_port=TCP_PORT, invite_type='LED DISPLAY', invite_id=1)
        # COPY FUN
        self._is_connected = self._network.tcp.is_connected
        self._get_my_ip = self._network.tcp.get_my_ip
        self._get_server_port = self._network.tcp.get_server_port
        self.launch = self._network.tcp.launch
        self.stop = self._network.tcp.stop

    def _event(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (ip, port) = value
                self.sign_connection.emit(is_connected, ip, port)

    def _error(self, module, code, value):
        self.sign_error.emit(module, code, value)

    def _recv(self, rx_msg, ip=None):
        pass

    def send(self, show):
        if show in LED_DISPLAY.keys():
            data = struct.pack('B', LED_DISPLAY[show])
            self._network.tcp.send(data)
