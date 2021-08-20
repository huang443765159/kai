import struct
import threading
from PyQt5.QtCore import QObject, pyqtSignal
from CarGuide.CARGUIDE.DRIVER.LocalSensor._OneSensor import OneSensor
from CarGuide.CARGUIDE.DRIVER.AutoNET.NetServer import NetServer
from CarGuide.CARGUIDE.DRIVER.AutoNET.NetInviter import NetInviter

MSG_HEAD = b'\xaa'


class LocalSensor(QObject):

    sign_sensors_data = pyqtSignal(dict)  # sensors data
    sign_sensor_data = pyqtSignal(int, int, int)  # sensor data

    sign_tcp_recv = pyqtSignal(bytes, str)  # bytes ip
    sign_tcp_event = pyqtSignal(bool, str, int)  # is_connected, ip, port
    sign_tcp_error = pyqtSignal(str, str, object)  # tcp, code, error

    def __init__(self, pin_list):
        super().__init__()
        self._pin_list = pin_list
        self._lock = threading.Lock()
        # SENSORS
        self._sensors = dict()
        self._sensors_data = dict()
        # self._new_sensors_data = dict()
        # self._sensors_memory_data = dict()
        for sid, pin in enumerate(pin_list):
            self._sensors_data[sid] = None
            self._sensors[sid] = OneSensor(sid=sid, pin=pin, lock=self._lock, data_cb=self._data_cb)
        self._net_server = NetServer(self._event_cb, self._error_cb, self._tcp_recv_cb, 8888)
        self._net_inviter = NetInviter(invite_type='Sensor', device_id=1)

    def _data_cb(self, sid, data):
        self._sensors_data[sid] = data
        if None not in self._sensors_data.values():
            new_sensors_data = dict()
            if new_sensors_data != self._sensors_data.copy():
                new_sensors_data = self._sensors_data.copy()
            # self._new_sensors_data = self._sensors_data.copy()
                self.sign_sensors_data.emit(new_sensors_data)
                self.sign_sensor_data.emit(list(new_sensors_data.values())[0],
                                           list(new_sensors_data.values())[1],
                                           list(new_sensors_data.values())[2])
                # self.sign_sensor_data.emit(list(new_sensors_data.values())[1])
                # self.sign_sensor_data.emit(list(new_sensors_data.values())[2])
                msg = MSG_HEAD + struct.pack('H', len(new_sensors_data))
                for sensor_data in new_sensors_data.values():
                    msg += struct.pack('H', sensor_data)
                self._net_server.tcp.send_broadcast(msg)
            for sid in self._sensors_data.keys():
                self._sensors_data[sid] = None
        # TEST 2
        # if self._sensors_memory_data != self._new_sensors_data:
        #     self._sensors_memory_data = self._new_sensors_data
        #     self.sign_sensors_data.emit(self._new_sensors_data)
        #     self.sign_sensor_data.emit(list(self._new_sensors_data.values())[0],
        #                                list(self._new_sensors_data.values())[1],
        #                                list(self._new_sensors_data.values())[2])
        #     msg = MSG_HEAD + struct.pack('H', len(self._new_sensors_data))
        #     for sensor_data in self._new_sensors_data.values():
        #         msg += struct.pack('H', sensor_data)
        #     self._net_server.tcp.send_broadcast(msg)

    def _event_cb(self, module, code, value):
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (ip, port) = value
                self.sign_tcp_event.emit(is_connected, ip, port)

    def _error_cb(self, module, code, value):
        self.sign_tcp_error.emit(module, code, value)

    def _tcp_recv_cb(self, rx_msg, ip):
        self.sign_tcp_recv.emit(rx_msg, ip)

    def thread_launch(self):
        for sensor in self._sensors.values():
            sensor.launch()

    def thread_stop(self):
        for sensor in self._sensors.values():
            sensor.stop()


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    local_sensor = LocalSensor([11, 16, 18])
    local_sensor.thread_launch()

    local_sensor.sign_sensors_data.connect(print)
    local_sensor.sign_sensor_data.connect(print)
    local_sensor.sign_tcp_event.connect(print)
    local_sensor.sign_tcp_error.connect(print)
    local_sensor.sign_tcp_recv.connect(print)

    sys.exit(app.exec_())
