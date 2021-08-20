import smbus
from PyQt5.QtCore import QObject, pyqtSignal
from QTimer任务流模块.DRIVER.AutoNET.NetServer import NetServer
from QTimer任务流模块.DRIVER.WashSwitchLocal._VirtualDance import VirtualDance

TCP_PORT = 20005
INSTRUCT = {0: 'ALL STOP', 1: 'WHEEL', 2: 'ALKALI CHEM', 3: 'ACID CHEM', 4: 'WATER WAX', 5: 'HIGH WATER', 6: 'START'}


class Relay(object):

    def __init__(self, relay_ip, relay_addr):
        self._relay_ip = relay_ip
        self._relay_addr = relay_addr
        # RELAY BUS
        self._bus = smbus.SMBus(1)

    def open(self):
        self._bus.write_byte_data(self._relay_ip, self._relay_addr, 0xff)

    def close(self):
        self._bus.write_byte_data(self._relay_ip, self._relay_addr, 0x00)


class WashSwitchLocal(QObject):

    sign_wash_type = pyqtSignal(str, bool)  # wash_type, switch
    sign_connection = pyqtSignal(bool, str, int)  # is_connected, ip, port
    sign_error = pyqtSignal(str, str, object)  # error_type, code, error

    def __init__(self, relays_ip, relays_addr):
        super().__init__()
        self._relays_ip = relays_ip
        self._relays_addr = relays_addr
        # RELAYS
        self._relays = list()
        for relay_ip in relays_ip:
            for relay_addr in relays_addr:
                relay = Relay(relay_ip=relay_ip, relay_addr=relay_addr)
                self._relays.append(relay)
        # WASH TYPE
        self._wash_type = None
        self._wash_types = {'ALL STOP': [relay for relay in self._relays],
                            'WHEEL': [self._relays[0], self._relays[4], self._relays[8]],
                            'ALKALI CHEM': [self._relays[1], self._relays[5], self._relays[9]],
                            'ACID CHEM': [self._relays[2], self._relays[6], self._relays[9]],
                            'WATER WAX': [self._relays[3], self._relays[7], self._relays[9]],
                            'HIGH WATER': [self._relays[10]]}
        # VIRTUAL DANCE
        self._dance = VirtualDance(event_cb=self._dance_event)
        self.dance_start = self._dance.start
        # ANET
        self._network = NetServer(event_cb=self._event, error_cb=self._error, tcp_recv_cb=self._recv, tcp_port=TCP_PORT)
        self.get_my_ip = self._network.tcp.get_my_ip
        self.connected = self._network.tcp.is_connected
        self.get_server_port = self._network.get_server_port
        self.get_client_ips = self._network.tcp.get_client_ips

    def _event(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (ip, port) = value
                self.sign_connection.emit(is_connected, ip, port)

    def _error(self, module, code, value):
        self.sign_error.emit(module, code, value)

    def _recv(self, rx_msg, ip=None):
        wash_type = rx_msg[0]
        switch = bool(rx_msg[1])
        if wash_type == 6:
            self.dance_start(wash_type='ALKALI CHEM')
        elif wash_type == 0:
            self.stop()
        else:
            if INSTRUCT[wash_type] in self._wash_types.keys():
                for relay in self._wash_types[INSTRUCT[wash_type]]:
                    relay.open() if switch else relay.close()
        self.sign_wash_type.emit(INSTRUCT[wash_type], switch)

    def _dance_event(self, wash_type, switch):
        self.sign_wash_type.emit(wash_type, switch)
        for relay in self._wash_types[wash_type]:
            relay.open() if switch else relay.close()
        if not switch:
            if wash_type == 'ALKALI CHEM':
                self.dance_start(wash_type='WHEEL', ts_duration=2)
            elif wash_type == 'WHEEL':
                self._wash_type = wash_type
                self.dance_start(wash_type='HIGH WATER', ts_duration=3)
            elif wash_type == 'HIGH WATER' and self._wash_type == 'WHEEL':
                self.dance_start(wash_type='ACID CHEM', ts_duration=5)
            elif wash_type == 'ACID CHEM':
                self._wash_type = wash_type
                self.dance_start(wash_type='HIGH WATER', ts_duration=3)
            elif wash_type == 'HIGH WATER' and self._wash_type == 'ACID CHEM':
                self.dance_start(wash_type='WATER WAX', ts_duration=2)
            elif wash_type == 'WATER WAX':
                self.dance_start(wash_type='HIGH WATER', ts_duration=3)
            else:
                self.sign_wash_type.emit('WASH FINISHED', True)

    def stop(self):
        for relay in self._wash_types['ALL STOP']:
            relay.close()
        self._dance.stop(switch=False)

    # TEST FUN
    def wheel(self, switch=True):
        for relay in self._wash_types['WHEEL']:
            relay.open() if switch else relay.close()

    def alkali_chem(self, switch=True):
        for relay in self._wash_types['ALKALI CHEM']:
            relay.open() if switch else relay.close()

    def acid_chem(self, switch=True):
        for relay in self._wash_types['ACID CHEM']:
            relay.open() if switch else relay.close()

    def water_wax(self, switch=True):
        for relay in self._wash_types['WATER WAX']:
            relay.open() if switch else relay.close()

    def high_water(self, switch=True):
        self._wash_types['HIGH WATER'][0].open() if switch else self._wash_types['HIGH WATER'][0].close()
