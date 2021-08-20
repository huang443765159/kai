import struct
from PyQt5.QtCore import QObject, pyqtSignal
from QTimer任务流模块.DRIVER.AutoNET.NetClient import NetClient

TCP_PORT = 20005
INSTRUCT = {'ALL STOP': 0, 'WHEEL': 1, 'ALKALI CHEM': 2, 'ACID CHEM': 3, 'WATER WAX': 4, 'HIGH WATER': 5, 'START': 6}


class WashSwitchNUC(QObject):

    sign_wash_type = pyqtSignal(str, bool)  # wash_type, switch
    sign_connection = pyqtSignal(bool, str, int)  # is_connected, ip, port
    sign_error = pyqtSignal(str, str, object)  # error_type, code, error

    def __init__(self, inviter_type='WASH'):
        super().__init__()
        self._inviter_type = inviter_type
        # NETWORK
        self._network = NetClient(event_cb=self._event, error_cb=self._error, tcp_recv_cb=self._recv,
                                  tcp_port=TCP_PORT, invite_type=inviter_type, invite_id=1)
        # COPY FUN
        self.get_my_id = self._network.get_my_ip
        self.get_server_ip = self._network.get_server_ip
        self.get_server_port = self._network.get_server_port
        self.launch = self._network.launch
        self.stop = self._network.stop

    def dance_start(self, switch):
        msg = struct.pack('B', INSTRUCT['START']) + struct.pack('?', switch)
        self._network.tcp.send(msg)

    def _event(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (ip, port) = value
                self.sign_connection.emit(is_connected, ip, port)

    def _error(self, module, code, value):
        self.sign_error.emit(module, code, value)

    def _recv(self, rx_msg, ip):
        self.sign_wash_type.emit(rx_msg)

    def get_inviter_type(self):
        return self._inviter_type

    # TEST
    def wheel(self, switch):
        msg = struct.pack('B', INSTRUCT['WHEEL']) + struct.pack('?', bool(switch))
        self._network.tcp.send(msg)

    def alkali_chem(self, switch):
        msg = struct.pack('B', INSTRUCT['ALKALI CHEM']) + struct.pack('?', bool(switch))
        self._network.tcp.send(msg)

    def acid_chem(self, switch):
        msg = struct.pack('B', INSTRUCT['ACID CHEM']) + struct.pack('?', bool(switch))
        self._network.tcp.send(msg)

    def water_wax(self, switch):
        msg = struct.pack('B', INSTRUCT['WATER WAX']) + struct.pack('?', bool(switch))
        self._network.tcp.send(msg)

    def high_water(self, switch):
        msg = struct.pack('B', INSTRUCT['HIGH WATER']) + struct.pack('?', bool(switch))
        self._network.tcp.send(msg)

    def all_stop(self):
        msg = struct.pack('B', INSTRUCT['ALL STOP']) + struct.pack('?', False)
        self._network.tcp.send(msg)
