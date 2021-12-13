import struct
from configparser import ConfigParser
from INTERACTIONS.XYZAutoNet.NetClient import NetClient
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from INTERACTIONS.NUC.PumpStations._PumpSwitch import PumpSwitch

TCP_PORT = 30000
DRAIN_HEAD = b'\x20'
LIQUID_HEAD = b'\x21'
PUMP_SWITCH_HEAD = b'\x22'
PUMP_COUNTDOWN = b'\x23'
LIQUID_TYPE = {0: 'WATER', 1: 'ALKALI', 2: 'ACID', 3: 'WHEEL', 4: 'WAX'}


class OnePumpStation(QObject):

    sign_drain_raw_data = pyqtSignal(list)  # drain_raw_data
    sign_liquid_raw_data = pyqtSignal(int, dict)  # bot_id, liquid_raw_data
    sign_pump_emit = pyqtSignal(int, str, bool)  # bot_id, instruct, is_open
    sign_pump_tcp_online = pyqtSignal(int, bool, str, int)  # bot_id, is_online, ip, port
    sign_pump_countdown = pyqtSignal(int, str, int)  # bot_id, instruct, countdown
    # sign_pump_tcp_error = pyqtSignal(int, str, str, object)  # bot_id, error_type, code, error

    def __init__(self, bot_id, config_dir, machine_sn, device_type='XYZ_PUMP_STATION', launch_delay=0.2):
        super().__init__()
        self._bot_id = bot_id
        self._config_dir = config_dir
        # NETWORK
        self._network = NetClient(event_cb=self._event, error_cb=self._error, tcp_recv_cb=self._recv, tcp_port=TCP_PORT)
        self._network.set_device_id(bot_id)
        self._network.set_device_type(device_type)
        self._network.set_device_token(machine_sn)
        # PUMP SWITCH
        self._pump_switch = PumpSwitch(bot_id=bot_id)
        self._pump_switch.sign_pump_emit.connect(self.sign_pump_emit)
        self._pump_switch.sign_pump_countdown.connect(self.sign_pump_countdown)
        # LOAD INI
        self.load_pump_ini()
        self._link = False
        # COPY FUNC
        self.exit = self._network.exit
        self.get_my_ip = self._network.get_my_ip
        self.get_server_ip = self._network.get_server_ip
        self.get_server_port = self._network.get_server_port
        QTimer.singleShot(int(launch_delay*1000), self._launch)

    def _launch(self):
        self._network.set_invitation_accepting_ena(True)

    def stop_all(self, is_open, t_wait):
        if self._link:
            msg = PUMP_SWITCH_HEAD + 'STOP_ALL'.encode() + struct.pack('?', is_open) + struct.pack('!H', t_wait)
            self._network.tcp.send(msg)
        else:
            self._pump_switch.set_pump_emit(instruct='STOP_ALL', is_open=is_open, t_wait=t_wait)

    def set_water_high_emit(self, is_open, t_wait):
        if self._link:
            msg = PUMP_SWITCH_HEAD + 'WATER_HIGH'.encode() + struct.pack('?', is_open) + struct.pack('!H', t_wait)
            self._network.tcp.send(msg)
        else:
            self._pump_switch.set_pump_emit(instruct='WATER_HIGH', is_open=is_open, t_wait=t_wait)

    def set_chem_alkali_emit(self, is_open, t_wait):
        if self._link:
            msg = PUMP_SWITCH_HEAD + 'CHEM_ALKALI'.encode() + struct.pack('?', is_open) + struct.pack('!H', t_wait)
            self._network.tcp.send(msg)
        else:
            self._pump_switch.set_pump_emit(instruct='CHEM_ALKALI', is_open=is_open, t_wait=t_wait)

    def set_chem_acid_emit(self, is_open, t_wait):
        if self._link:
            msg = PUMP_SWITCH_HEAD + 'CHEM_ACID'.encode() + struct.pack('?', is_open) + struct.pack('!H', t_wait)
            self._network.tcp.send(msg)
        else:
            self._pump_switch.set_pump_emit(instruct='CHEM_ACID', is_open=is_open, t_wait=t_wait)

    def set_wheel_emit(self, is_open, t_wait):
        if self._link:
            msg = PUMP_SWITCH_HEAD + 'WHEEL'.encode() + struct.pack('?', is_open) + struct.pack('!H', t_wait)
            self._network.tcp.send(msg)
        else:
            self._pump_switch.set_pump_emit(instruct='WHEEL', is_open=is_open, t_wait=t_wait)

    def set_water_wax_emit(self, is_open, t_wait):
        if self._link:
            msg = PUMP_SWITCH_HEAD + 'WATER_WAX'.encode() + struct.pack('?', is_open) + struct.pack('!H', t_wait)
            self._network.tcp.send(msg)
        else:
            self._pump_switch.set_pump_emit(instruct='WATER_WAX', is_open=is_open, t_wait=t_wait)

    def set_drain_emit(self, is_open, t_wait):
        if self._link:
            msg = PUMP_SWITCH_HEAD + 'DRAIN'.encode() + struct.pack('?', is_open) + struct.pack('!H', t_wait)
            self._network.tcp.send(msg)
        else:
            self._pump_switch.set_pump_emit(instruct='DRAIN', is_open=is_open, t_wait=t_wait)

    def set_water_inflow_emit(self, is_open, t_wait):
        if self._link:
            msg = PUMP_SWITCH_HEAD + 'WATER_INFLOW'.encode() + struct.pack('?', is_open) + struct.pack('!H', t_wait)
            self._network.tcp.send(msg)
        else:
            self._pump_switch.set_pump_emit(instruct='WATER_INFLOW', is_open=is_open, t_wait=t_wait)

    def _event(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (server_ip, server_port) = value
                self.sign_pump_tcp_online.emit(self._bot_id, is_connected, server_ip, server_port)

    def _error(self, module, code, value):
        pass

    def _recv(self, rx_msg, ip):
        if self._link:
            msg_head = rx_msg[0:1]
            drain_raw_data = list()
            liquid_raw_data = dict()
            if msg_head == DRAIN_HEAD:
                data_len = struct.unpack('B', rx_msg[1: 2])[0]
                for i in range(data_len):
                    data = struct.unpack('?', rx_msg[i + 2: i + 3])[0]
                    drain_raw_data.append(data)
                self.sign_drain_raw_data.emit(drain_raw_data)
            elif msg_head == LIQUID_HEAD:
                data_len = struct.unpack('B', rx_msg[1: 2])[0]
                for i in range(data_len):
                    data = struct.unpack('!H', rx_msg[i * 2 + 2: i * 2 + 4])[0]
                    liquid_raw_data[LIQUID_TYPE[i]] = data
                self.sign_liquid_raw_data.emit(self._bot_id, liquid_raw_data)
            elif msg_head == PUMP_SWITCH_HEAD:
                pump_instruct = rx_msg[1: -1].decode()
                switch = bool(rx_msg[-1])
                self.sign_pump_emit.emit(self._bot_id, pump_instruct, switch)
            elif msg_head == PUMP_COUNTDOWN:
                instruct = rx_msg[1: -2].decode()
                t_wait = struct.unpack('!H', rx_msg[-2: ])[0]
                self.sign_pump_countdown.emit(self._bot_id, instruct, t_wait)

    def set_link(self, link):
        self._link = bool(link)
        if link:
            self._pump_switch.sign_pump_emit.disconnect(self.sign_pump_emit)
            self._pump_switch.sign_pump_countdown.disconnect(self.sign_pump_countdown)
        else:
            self._pump_switch.sign_pump_emit.connect(self.sign_pump_emit)
            self._pump_switch.sign_pump_countdown.connect(self.sign_pump_countdown)

    def get_link(self):
        return self._link

    def load_pump_ini(self):
        pump_ini_path = f'{self._config_dir}/Pump{self._bot_id}.ini'
        pump_ini = ConfigParser()
        pump_ini.read(pump_ini_path)
        for instruct in ['WATER_HIGH', 'CHEM_ALKALI', 'CHEM_ACID', 'WATER_WAX', 'WHEEL', 'DRAIN', 'WATER_INFLOW']:
            self._pump_switch.load_ini(instruct, pump_ini.getfloat(instruct, 't_delay'))

    def save_pump_ini(self):
        pump_ini_path = f'{self._config_dir}/PUMP{self._bot_id}.ini'
        pump_ini = ConfigParser()
        pump_ini.read(pump_ini_path)
        for instruct in ['WATER_HIGH', 'CHEM_ALKALI', 'CHEM_ACID', 'WATER_WAX', 'WHEEL', 'DRAIN', 'WATER_INFLOW']:
            pump_ini.set(instruct, 't_delay', f'{self._pump_switch.get_t_delay()}')
            with open(pump_ini_path, 'w') as file_obj:
                pump_ini.write(file_obj)

    def set_turbo(self, turbo):
        self._pump_switch.set_turbo(turbo=turbo)
        self.load_pump_ini()

    def get_turbo(self):
        return self._pump_switch.get_turbo()

    def exit(self):
        self.stop_all(is_open=False, t_wait=0)
        self._network.exit()
