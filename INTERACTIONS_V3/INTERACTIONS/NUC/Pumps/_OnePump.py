import struct
from configparser import ConfigParser
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from INTERACTIONS.XYZAutoNet.NetClient import NetClient
from INTERACTIONS.NUC.Pumps._MathOnePump import MathOnePump

TCP_PORT = 30000
HEAD_LIQUID_LEVEL = b'\x21'
HEAD_PUMP_SWITCH = b'\x22'
HEAD_ALL_STOP = b'\x23'
HEAD_REMAIN_TS = b'\x24'
HEAD_LOAD_INI = b'\x25'
HEAD_SAVE_INI = b'\x26'
LIQUID_WATER_HIGH = 0
LIQUID_CH_A = 1
LIQUID_CH_B = 2
LIQUID_CH_WHL = 3
LIQUID_CH_WAX = 4
LIQUID_DRAIN = 5

"""
TS 定义
extra_ts: NUC层在get到APP层水泵到喷射出来的剩余时间后，要设置的延迟时间
ts_remain: 泵到喷射出来的剩余时间，在GUI层会进行倒计时，如果用户在设置extra_ts后，ts_remain会加上extra_ts时间后再进行倒计时
math_ts_to_jet：人工测量出来直接开泵到喷射出液体的时间，存在ini里，不可变
"""


class OnePump(QObject):

    sensor_level = pyqtSignal(int, int, int)  # bot_id, sensor_id, sensor_level
    sign_pump_shooting = pyqtSignal(int, int, bool)  # bot_id, liquid_id, switch
    sign_pump_remain_ts = pyqtSignal(int, int, float, float)  # bot_id, liquid_id, remain_ts, extra_ts
    sign_tcp_online = pyqtSignal(int, bool, str, int)  # bot_id, is_online, ip, port

    def __init__(self, bot_id, config_dir, machine_sn, device_type='XYZ_PUMP_STATION', launch_delay=0.2):
        super().__init__()
        self._bot_id = bot_id
        self._config_dir = config_dir
        # NETWORK
        self._network = NetClient(event_cb=self._event, error_cb=self._error, tcp_recv_cb=self._recv, tcp_port=TCP_PORT)
        self._network.set_device_id(bot_id)
        self._network.set_device_type(device_type)
        self._network.set_device_token(machine_sn)
        # PUMP_SWITCH
        self._math_pump = MathOnePump(bot_id=bot_id, config_dir=config_dir)
        self._math_pump.sign_pump_shooting.connect(self.sign_pump_shooting)
        self._math_pump.sign_pump_remain_ts.connect(self.sign_pump_remain_ts)
        # LOAD_INI
        self._sensors_level = dict()
        self._pump_remain_ts = dict()
        # COPY_FUNC
        QTimer.singleShot(int(launch_delay * 1000), lambda: self._network.set_invitation_accepting_ena(True))

    # FUNC
    def set_pump_shooting(self, liquid_id, switch, extra_ts=0.0):
        if self.get_link():
            msg = HEAD_PUMP_SWITCH + struct.pack('B', liquid_id) + struct.pack('?', switch) + struct.pack('!e', extra_ts)
            self._network.tcp.send(msg)
        else:
            self._math_pump.set_pump_shooting(liquid_id=liquid_id, switch=switch, extra_ts=extra_ts)

    def get_liquid_remain_ts(self, liquid_id):
        if self.get_link():
            if liquid_id in self._pump_remain_ts.keys():
                return self._pump_remain_ts[liquid_id]
            else:
                return self._math_pump.get_ts_to_jet(liquid_id)
        else:
            return self._math_pump.get_pump_remain_ts(liquid_id=liquid_id)

    def stop_all(self):
        self._network.tcp.send(HEAD_ALL_STOP)
        self._math_pump.stop_all()

    def set_link(self, link):
        self.stop_all()
        self._math_pump.set_link(link=link)

    def get_link(self):
        return self._math_pump.get_link()

    def set_turbo(self, turbo):
        self._math_pump.set_turbo(turbo=turbo)

    def get_turbo(self):
        return self._math_pump.get_turbo()

    def get_sensors_level(self):
        return self._sensors_level

    def set_ts_to_jet(self, liquid_id, ts_to_jet: float):
        self._math_pump.set_ts_to_jet(liquid_id, ts_to_jet)

    def get_ts_to_jet(self, liquid_id):
        return self._math_pump.get_ts_to_jet(liquid_id=liquid_id)

    # LOAD INI
    def load_pump_ini(self):
        pump_ini_path = f'{self._config_dir}/Pump{self._bot_id}.ini'
        pump_ini = ConfigParser()
        pump_ini.read(pump_ini_path)
        for liquid_id, ini_type in enumerate(
                ['LIQUID_WATER_HIGH', 'LIQUID_CH_A', 'LIQUID_CH_B', 'LIQUID_CH_WHL', 'LIQUID_CH_WAX']):
            self._math_pump.set_ts_to_jet(liquid_id, pump_ini.getfloat(ini_type, 'math_ts_to_jet'))
            msg = HEAD_LOAD_INI + struct.pack('B', liquid_id) + struct.pack('!e', pump_ini.getfloat(ini_type, 'math_ts_to_jet'))
            self._network.tcp.send(msg)

    def save_pump_ini(self, peer_save=True):
        pump_ini_path = f'{self._config_dir}/Pump{self._bot_id}.ini'
        pump_ini = ConfigParser()
        pump_ini.read(pump_ini_path)
        for liquid_id, ini_type in enumerate(
                ['LIQUID_WATER_HIGH', 'LIQUID_CH_A', 'LIQUID_CH_B', 'LIQUID_CH_WHL', 'LIQUID_CH_WAX']):
            pump_ini.set(ini_type, 'math_ts_to_jet', f'{self._math_pump.get_ts_to_jet(liquid_id)}')
            if peer_save:
                msg = HEAD_SAVE_INI + struct.pack('B', liquid_id) + struct.pack(
                    '!e', (self._math_pump.get_ts_to_jet(liquid_id)))
                self._network.tcp.send(msg)
        with open(pump_ini_path, 'w') as file_obj:
            pump_ini.write(file_obj)

    # NETWORK
    def _event(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (server_ip, server_port) = value
                self.sign_tcp_online.emit(self._bot_id, is_connected, server_ip, server_port)

    def _error(self, module, code, value):
        pass

    def _recv(self, rx_msg, ip):
        head = rx_msg[0: 1]
        if head == HEAD_REMAIN_TS:
            liquid_id = struct.unpack('B', rx_msg[1: 2])[0]
            remain_ts = struct.unpack('!e', rx_msg[2: 4])[0]
            extra_ts = struct.unpack('!e', rx_msg[4: 6])[0]
            self._pump_remain_ts[liquid_id] = remain_ts
            if self.get_link():
                self.sign_pump_remain_ts.emit(self._bot_id, liquid_id, remain_ts, extra_ts)
        elif head == HEAD_LIQUID_LEVEL:
            sensor_id = struct.unpack('B', rx_msg[1: 2])[0]
            sensor_level = struct.unpack('B', rx_msg[2: 3])[0]
            self.sensor_level.emit(self._bot_id, sensor_id, sensor_level)
            self._sensors_level[sensor_id] = sensor_level
        if self.get_link():
            if head == HEAD_PUMP_SWITCH:
                liquid_id = struct.unpack('B', rx_msg[1: 2])[0]
                switch = struct.unpack('?', rx_msg[2: 3])[0]
                self.sign_pump_shooting.emit(self._bot_id, liquid_id, switch)

    def exit(self):
        self.stop_all()
        self._network.exit()
