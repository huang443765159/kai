import struct
from INTERACTIONS.XYZAutoNet.NetClient import NetClient
from PyQt5.QtCore import QObject, pyqtSignal

TCP_PORT = 30000
DRAIN_HEAD = b'\x20'
LIQUID_HEAD = b'\x21'
PUMP_SWITCH_HEAD = b'\x22'
LIQUID_TYPE = {0: 'WATER', 1: 'ALKALI', 2: 'ACID', 3: 'WHEEL', 4: 'WAX'}


class OnePumpStation(QObject):

    sign_drain_raw_data = pyqtSignal(list)  # drain_raw_data
    sign_liquid_raw_data = pyqtSignal(int, dict)  # device_id, liquid_raw_data
    sign_pump_instruction = pyqtSignal(int, str, bool)  # device_id, pump_instruct, is_open
    sign_pump_tcp_online = pyqtSignal(int, bool, str, int)  # device_id, is_online, ip, port
    sign_pump_tcp_error = pyqtSignal(int, str, str, object)  # device_id, error_type, code, error

    def __init__(self, device_id, machine_sn, device_type='XYZ-PUMP STATION'):
        super().__init__()
        self._device_id = device_id
        # NETWORK
        self._network = NetClient(event_cb=self._event, error_cb=self._error, tcp_recv_cb=self._recv, tcp_port=TCP_PORT)
        self._network.set_device_id(device_id)
        self._network.set_device_type(device_type)
        self._network.set_device_token(machine_sn)
        self._network.set_invitation_accepting_ena(True)
        # COPY FUNC
        self.exit = self._network.exit
        self.get_my_ip = self._network.get_my_ip
        self.get_server_ip = self._network.get_server_ip
        self.get_server_port = self._network.get_server_port

    def pump_instruction(self, pump_instruct, is_open):
        msg = PUMP_SWITCH_HEAD + pump_instruct.encode() + struct.pack('?', is_open)
        self._network.tcp.send(msg)

    def _event(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (server_ip, server_port) = value
                self.sign_pump_tcp_online.emit(self._device_id, is_connected, server_ip, server_port)

    def _error(self, module, code, value):
        self.sign_pump_tcp_error.emit(self._device_id, module, code, value)

    def _recv(self, rx_msg, ip):
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
            self.sign_liquid_raw_data.emit(self._device_id, liquid_raw_data)
        elif msg_head == PUMP_SWITCH_HEAD:
            pump_instruct = rx_msg[1: -1].decode()
            switch = bool(rx_msg[-1])
            self.sign_pump_instruction.emit(self._device_id, pump_instruct, switch)

    def exit(self):
        self._network.exit()
