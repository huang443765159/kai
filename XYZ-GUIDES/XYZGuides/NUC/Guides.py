import struct
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from XYZAutoNet.NetClient import NetClient

TCP_PORT = 20013
RAW_DATA_HEAD = b'\xaa'


class Guides(QObject):

    sign_raw_data = pyqtSignal(list)  # raw_data
    sign_stage_changed = pyqtSignal(int)  # stage_id
    sign_tcp_error = pyqtSignal(str, str, object)  # error_type, code, error
    sign_tcp_online = pyqtSignal(bool, str, int)  # is_online, peer_ip, peer_port

    def __init__(self, machine_sn, device_type='XYZ-GUIDES'):
        super().__init__()
        # ANET
        self._network = NetClient(event_cb=self._event, error_cb=self._error, tcp_recv_cb=self._recv, tcp_port=TCP_PORT)
        self._network.set_device_id(2)
        self._network.set_device_type(device_type)
        self._network.set_device_token(machine_sn)
        # COPY FUN
        self.get_my_ip = self._network.get_my_ip
        self.get_server_ip = self._network.get_server_ip
        self.get_server_port = self._network.get_server_port
        QTimer.singleShot(200, self._launch)

    def _launch(self):
        self._network.set_invitation_accepting_ena(True)

    def _event(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (server_ip, server_port) = value
                self.sign_tcp_online.emit(is_connected, server_ip, server_port)

    def _error(self, module, code, value):
        self.sign_tcp_error.emit(module, code, value)

    def _recv(self, rx_msg, ip=None):
        if rx_msg[0:1] == RAW_DATA_HEAD:
            raw_data = list()
            data_len = struct.unpack('B', rx_msg[1:2])[0]
            for i in range(data_len):
                _data = struct.unpack('?', rx_msg[2 + i:3 + i])[0]
                raw_data.append(_data)
            self.sign_raw_data.emit(raw_data)
        else:
            stage_id = struct.unpack('B', rx_msg)[0]
            self.sign_stage_changed.emit(stage_id)

    def exit(self):
        self._network.exit()

    # TEST
    def set_stage_id_for_test(self, stage_id):
        msg = struct.pack('B', stage_id)
        self._network.tcp.send(msg)
