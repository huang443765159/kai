import signal
import struct
from PyQt5.QtCore import QObject, pyqtSignal
from V2.DRIVER.AutoNET.NetClient import NetClient

MSG_HEAD = b'\xaa'


class RemoteSensor(QObject):

    sign_connect = pyqtSignal(bool, str, int)  # is_connected, ip, port
    sign_error = pyqtSignal(str, str, object)  # tcp, code, err
    sign_sensors_data = pyqtSignal(dict)  # sensors data dict
    sign_sensor_data = pyqtSignal(int, int, int)  # every sensor data

    sign_sys_quit = pyqtSignal(str)  # sys_quit

    def __init__(self):
        super().__init__()
        self._net_client = NetClient(self._event_cb,
                                     self._error_cb,
                                     self._tcp_recv_cb,
                                     8888, 'Sensor', 1)
        self._signal = signal.signal(signal.SIGINT, self._sys_quit)

    def _event_cb(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (ip, port) = value
                print(is_connected, (ip, port))
                self.sign_connect.emit(is_connected, ip, port)

    def _error_cb(self, module, code, value):
        # print(module, code, value)
        self.sign_error.emit(module, code, value)

    def _tcp_recv_cb(self, rx_msg, ip):
        if rx_msg[0:1] == MSG_HEAD:
            sensor_data_len = struct.unpack('H', rx_msg[1:3])[0]
            sensors_data_dict = dict()
            count = 0
            for i in range(sensor_data_len):
                count += 2
                sensors_data = struct.unpack('H', rx_msg[1+count:3+count])[0]
                sensors_data_dict[i] = sensors_data
            # print(sensors_data_dict)
            self.sign_sensors_data.emit(sensors_data_dict)
            # print(list(sensors_data_dict.values()))
            self.sign_sensor_data.emit(list(sensors_data_dict.values())[0],
                                       list(sensors_data_dict.values())[1],
                                       list(sensors_data_dict.values())[2])
            # self._net_client.tcp.send(b'\xbb')

    def _sys_quit(self, signal_num, handle):
        # print('Sys Quit')
        self.sign_sys_quit.emit('SYS QUIT')
        sys.exit(0)


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    remote_sensor = RemoteSensor()
    remote_sensor.sign_sensors_data.connect(print)
    remote_sensor.sign_sensor_data.connect(print)
    remote_sensor.sign_connect.connect(print)
    remote_sensor.sign_error.connect(print)
    remote_sensor.sign_sys_quit.connect(print)
    # while 1:
    #     time.sleep(1)

    sys.exit(app.exec_())
