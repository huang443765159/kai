import struct
import signal
from PyQt5.QtCore import QObject, pyqtSignal
from CarGuide.V2.DRIVER.LocalSensor._OneSensor import OneSensor
from CarGuide.V2.DRIVER.AutoNET.NetServer import NetServer
from CarGuide.V2.DRIVER.AutoNET.NetInviter import NetInviter

MSG_HEAD = b'\xaa'


class LocalSensor(QObject):

    sign_connect = pyqtSignal(bool, str, int)  # is_connected, ip, port
    sign_error = pyqtSignal(str, str, object)  # TCP, CODE, ERR
    sign_recv = pyqtSignal(bytes, str)  # bytes, ip
    sign_sensors_data = pyqtSignal(dict)  # sensors data dict
    sign_sensor_data = pyqtSignal(int, int, int)  # every sensor data

    sign_sys_quit = pyqtSignal(str)  # sys quit

    def __init__(self, pin_list):
        super(). __init__()

        self._pin_list = pin_list
        self._sensors = dict()
        self._sensors_data = dict()
        self._sensors_memory_data = dict()
        for sid, pin in enumerate(self._pin_list):
            self._sensors[sid] = OneSensor(sid=sid, pin=pin, data_cb=self._data_cb)
            self._sensors_data[sid] = None
            self._sensors_memory_data[sid] = None

        self._net_server = NetServer(self._event_cb, self._error_cb, self._tcp_recv_cb, 8888)
        self._net_inviter = NetInviter(invite_type='Sensor', device_id=1)
        self._signal = signal.signal(signal.SIGINT, self._sys_quit)

    def _data_cb(self, sid, data):
        self._sensors_data[sid] = data
        if None not in self._sensors_data.values():
            # print(self._sensors_data)
            new_sensor_data = self._sensors_data.copy()
            self.sign_sensors_data.emit(new_sensor_data)
            # print(list(self._sensors_data.values()))
            self.sign_sensor_data.emit(list(self._sensors_data.values())[0],
                                       list(self._sensors_data.values())[1],
                                       list(self._sensors_data.values())[2])
            msg = MSG_HEAD + struct.pack('H', len(self._sensors_data))
            for data in self._sensors_data.values():
                msg += struct.pack('H', data)
            self._net_server.tcp.send_broadcast(msg)
            for sid in self._sensors_data.keys():
                self._sensors_data[sid] = None

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
        # print(rx_msg, ip)
        self.sign_recv.emit(rx_msg, ip)

    def launch(self):
        for sensor in self._sensors.values():
            sensor.launch()

    def stop(self):
        for sensor in self._sensors.values():
            sensor.stop()

    def _sys_quit(self, signal_num, handle):
        # print('Sys Quit')
        self.sign_sys_quit.emit('SYS QUIT')
        sys.exit(0)


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    _pin_list = [1, 2, 3]
    local_sensor = LocalSensor(_pin_list)
    local_sensor.launch()

    local_sensor.sign_sensors_data.connect(print)
    local_sensor.sign_sensor_data.connect(print)
    local_sensor.sign_connect.connect(print)
    local_sensor.sign_error.connect(print)
    local_sensor.sign_recv.connect(print)
    local_sensor.sign_sys_quit.connect(print)
    # while 1:
    #     time.sleep(2)
    sys.exit(app.exec_())
