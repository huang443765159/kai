import struct
from PyQt5.QtCore import QObject, pyqtSignal
from INTERACTIONS.DRIVER.AutoNET.NetClient import NetClient

TCP_PORT = 20013


class Guides(QObject):

    sign_data = pyqtSignal(list)  # guides_data
    sign_event = pyqtSignal(str, str, tuple)  # event_type, code, value
    sign_error = pyqtSignal(str, str, object)  # error_type, code, error

    def __init__(self, device_type, device_token):
        super().__init__()
        self._device_type = device_type
        self._device_token = device_token
        # ANET
        self._network = NetClient(event_cb=self._event, error_cb=self._error, tcp_recv_cb=self._recv, tcp_port=TCP_PORT)
        self._network.set_device_id(1)
        self._network.set_invitation_accepting_ena(True)
        self._network.set_device_type(self._device_type)
        self._network.set_device_token(self._device_token)
        # COPY FUN
        self.get_my_ip = self._network.get_my_ip
        self.get_server_ip = self._network.get_server_ip
        self.get_server_port = self._network.get_server_port

    def _event(self, module, code, value):
        self.sign_event.emit(module, code, value)

    def _error(self, module, code, value):
        self.sign_error.emit(module, code, value)

    def _recv(self, rx_msg, ip=None):
        data_len = rx_msg[0]
        guides_data = list()
        for i in range(data_len):
            data = struct.unpack('?', rx_msg[i + 1: i + 2])[0]
            guides_data.append(data)
        self.sign_data.emit(guides_data)

    def exit(self):
        self._network.exit()
