import time
import struct
from PyQt5.QtCore import pyqtSignal, QObject
from CarGuide.V1.DRIVER.AutoNET.NetClient import NetClient

MSG_HEAD = b'\xbb'
DATA_ZOOM = 100


class UltraSonicRemote(QObject):

    sign_server_error = pyqtSignal(str, str, object)  # tcp, state, err
    sign_connection = pyqtSignal(bool, str, int)  # is_connected, peer_ip, peer_port

    sign_sensors_data = pyqtSignal(dict)  # data_dict
    sign_sensor_data = pyqtSignal(float, float, float)  # sensors data

    def __init__(self):
        super().__init__()

        self._net_client = NetClient(tcp_recv_cb=self._recv_cb,
                                     tcp_port=8888,
                                     invite_type='Sensor', device_id=8,
                                     event_cb=self._event_cb,
                                     error_cb=self._error_cb)

    def _event_cb(self, module, code, value):
        # print(module, code, value)
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (server_ip, server_port) = value
                self.sign_connection.emit(is_connected, server_ip, server_port)

    def _error_cb(self, module, code, value):
        # print(module, code, value)
        self.sign_server_error.emit(module, code, value)

    def _recv_cb(self, rx_msg, ip):
        if rx_msg[0] == 0xbb:
            data_sum = struct.unpack('H', rx_msg[1:3])[0]
            num_stand = 0
            data_dict = dict()
            for i in range(data_sum):
                num_stand += 2
                data = struct.unpack('H', rx_msg[1+num_stand:3+num_stand])[0]
                data_dict[i] = float(data/DATA_ZOOM)
            self.sign_sensors_data.emit(data_dict)
            # print(data_dict)
            data_list = list()
            for data in data_dict.values():
                data_list.append(data)
            # print(data_list)
            self.sign_sensor_data.emit(data_list[0], data_list[1], data_list[2])


if __name__ == '__main__':
    one_sensor = UltraSonicRemote()
    while 1:
        time.sleep(1)



