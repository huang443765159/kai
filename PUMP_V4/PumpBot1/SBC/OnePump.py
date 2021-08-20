import struct
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from PumpBot1.SBC._Channels import Channels
from PumpBot1.Util.DEFINES import NETWORK as NET
from PumpBot1.XYZAutoNet.NetServer import NetServer

TCP_PORT = 30000


class OnePump(QObject):

    sign_sensor_level = pyqtSignal(int, int, int)  # bot_id, sensor_id, liquid_level
    sign_channel_ena = pyqtSignal(int, int, int)  # bot_id, cid, state(0, 1)
    sign_tcp_online = pyqtSignal(bool, str, int)  # is_online, ip, port

    def __init__(self, config_dir, bot_id, machine_sn, device_type='XYZ_PUMP_STATION', delay_launch=0.2):
        super().__init__()
        self._config_dir = config_dir
        self._bot_id = bot_id
        # NETWORK
        self._network = NetServer(event_cb=self._event, error_cb=self._error, tcp_recv_cb=self._recv, tcp_port=TCP_PORT)
        self._network.set_device_id(bot_id)
        self._network.set_device_type(device_type)
        self._network.set_device_token(machine_sn)
        # PUMP
        self._channels = Channels(bot_id=bot_id, config_dir=config_dir)
        self._channels.sign_channel_ena.connect(self.sign_channel_ena)
        QTimer.singleShot(int(delay_launch * 1000), lambda: self._network.set_invitation_broadcast_ena(True))

    def exit(self):
        self._channels.stop_all()
        self._network.exit()

    def stop_all(self):
        self._channels.stop_all()

    # STATE
    def get_calibration_ts(self):
        return self._channels.ts_calibration

    # NETWORK
    def _event(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (server_ip, server_port) = value
                self.sign_tcp_online.emit(is_connected, server_ip, server_port)

    def _error(self, module, code, value):
        pass

    def _recv(self, rx_msg, ip):
        msg_head = rx_msg[0: 1]
        if msg_head == NET.PUMP_ENA:
            cid = struct.unpack('B', rx_msg[1: 2])[0]
            ena = struct.unpack('?', rx_msg[2: 3])[0]
            self._channels.set_channel_ena(cid=cid, ena=ena)

    # TEST_FUNC
    def set_pump_ena(self, liquid_id, ena):
        self._channels.set_channel_ena(cid=liquid_id, ena=ena)
