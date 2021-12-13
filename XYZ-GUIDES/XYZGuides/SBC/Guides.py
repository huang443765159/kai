from platform import system
if 'Darwin' in system():
    PI_GPIO = None
elif 'Linux' in system():
    PI_GPIO = 1
import struct
from XYZAutoNet.NetServer import NetServer
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from XYZGuides.SBC._Sensors import Sensors

TCP_PORT = 20013
RAW_DATA_HEAD = b'\xaa'
STAGES = {0x10: '欢迎光临', 0x11: '向前行驶', 0x12: '停止行驶', 0x13: '向后行驶', 0x14: '正在清洗', 0x15: '清洗结束'}


class Guides(QObject):

    sign_raw_data = pyqtSignal(list)  # raw_data
    sign_stage_changed = pyqtSignal(int)  # stage_id
    sign_tcp_error = pyqtSignal(str, str, object)  # error_type, code, error
    sign_tcp_online = pyqtSignal(bool, str, int)  # is_online, peer_ip, peer_port

    def __init__(self, machine_sn, device_type='XYZ-GUIDES', pins=(21, 26)):
        super().__init__()
        # NETWORK
        self._network = NetServer(event_cb=self._event, error_cb=self._error, tcp_recv_cb=self._recv, tcp_port=TCP_PORT)
        self._network.set_device_id(2)
        self._network.set_device_type(device_type)
        self._network.set_device_token(machine_sn)
        # GUIDES
        self._guides = Sensors(pi_gpio=PI_GPIO, pins=pins)
        self._guides.sign_raw_data.connect(self._raw_data_analysis)
        # ATTR
        self._data_memory = True
        # COPY FUN
        self.get_my_ip = self._network.get_my_ip
        self.get_client_ips = self._network.get_client_ips
        self.get_server_port = self._network.get_server_port
        QTimer.singleShot(200, self._launch)

    def _launch(self):
        self._network.set_invitation_broadcast_ena(True)

    def _raw_data_analysis(self, raw_data):
        self.sign_raw_data.emit(raw_data)
        msg = RAW_DATA_HEAD + struct.pack('B', len(raw_data))
        for _data in raw_data:
            msg += struct.pack('?', _data)
        self._network.tcp.send_broadcast(msg)
        stage_id = None
        if not raw_data[0] and raw_data[1]:
            stage_id = 0x11
            self._data_memory = raw_data[0]
        if not self._data_memory and raw_data[0] and raw_data[1]:
            stage_id = 0x12
        if raw_data[0] and not raw_data[1]:
            stage_id = 0x13
        if stage_id is not None:
            self.sign_stage_changed.emit(stage_id)
            msg = struct.pack('B', stage_id)
            self._network.tcp.send_broadcast(msg)

    def _event(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (server_ip, server_port) = value
                self.sign_tcp_online.emit(is_connected, server_ip, server_port)

    def _error(self, module, code, value):
        self.sign_tcp_error.emit(module, code, value)

    def _recv(self, rx_msg, ip=None):
        stage_id = struct.unpack('B', rx_msg)[0]
        self.sign_stage_changed.emit(stage_id)
        # self.set_stage_id_for_test(stage_id=stage_id)

    def exit(self):
        self._network.exit()
        self._guides.exit()

    # USE_FOR_TEST
    def set_stage_id_for_test(self, stage_id):
        msg = struct.pack('B', stage_id)
        self._network.tcp.send_broadcast(msg)
