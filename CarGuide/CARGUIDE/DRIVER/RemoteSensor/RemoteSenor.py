import struct
from PyQt5.QtCore import QObject, pyqtSignal
from CarGuide.CARGUIDE.DRIVER.AutoNET.NetClient import NetClient

MSG_HEAD = b'\xaa'


class RemoteSensor(QObject):

    sign_sensors_data = pyqtSignal(dict)  # sensors data
    sign_sensor_data = pyqtSignal(int, int, int)  # sensor data

    sign_tcp_event = pyqtSignal(bool, str, int)  # is_connected, ip, port
    sign_tcp_error = pyqtSignal(str, str, object)  # tcp, code, error

    def __init__(self):
        super().__init__()

        self._net_client = NetClient(self._event_cb, self._error_cb, self._tcp_recv_cb, 8888, 'Guide', 1)

    def _event_cb(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (ip, port) = value
                self.sign_tcp_event.emit(is_connected, ip, port)

    def _error_cb(self, module, code, value):
        self.sign_tcp_error.emit(module, code, value)

    def _tcp_recv_cb(self, rx_msg, ip):
        if rx_msg[0:1] == MSG_HEAD:
            data_len = struct.unpack('H', rx_msg[1:3])[0]
            sensors_data = dict()
            count = 0
            for i in range(data_len):
                count += 2
                sensor_data = struct.unpack('H', rx_msg[1 + count:3 + count])[0]
                sensors_data[i] = sensor_data
            self.sign_sensors_data.emit(sensors_data)
            self.sign_sensor_data.emit(list(sensors_data.values())[0],
                                       list(sensors_data.values())[1],
                                       list(sensors_data.values())[2])


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    remote_sensor = RemoteSensor()
    remote_sensor.sign_sensors_data.connect(print)
    remote_sensor.sign_sensor_data.connect(print)
    remote_sensor.sign_tcp_event.connect(print)
    remote_sensor.sign_tcp_error.connect(print)

    sys.exit(app.exec_())
