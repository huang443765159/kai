import time
import struct
from PyQt5.QtCore import QObject, pyqtSignal
from CarGuide.V1.DRIVER.AutoNET.NetServer import NetServer
from CarGuide.V1.DRIVER.AutoNET.NetInviter import NetInviter
from CarGuide.V1.DRIVER.UltraSonicLocal._OneSensor import OneSensor

MSG_HEAD = b'\xbb'
DATA_ZOOM = 100


class UltraSonicLocal(QObject):

    sign_sensors_data = pyqtSignal(list)  # sensors_data
    sign_sensor_data = pyqtSignal(float, float, float)  # sensor_data

    sign_server_error = pyqtSignal(str, str, object)  # tcp, state, err
    sign_server_recv = pyqtSignal(object, object)
    sign_connection = pyqtSignal(bool, str, int)  # is_connected, peer_ip, peer_port

    def __init__(self, pin_list):
        super().__init__()

        self._net_server = NetServer(self._event_cb, self._error_cb, self._tcp_recv_cb, 8888)
        self._inviter = NetInviter(invite_type='Sensor', device_id=8, event_cb=self._event_cb)

        self._pin_list = pin_list
        self._sensors = dict()
        self._sensors_data = dict()
        for sid, pin in enumerate(self._pin_list):
            self._sensors[sid] = OneSensor(sid=sid, pin=pin, data_cb=self._data_cb)
            self._sensors_data[sid] = None

    def _data_cb(self, sid, data):
        self._sensors_data[sid] = data
        if None not in list(self._sensors_data.values()):
            print(self._sensors_data)
            tcp_msg = MSG_HEAD
            tcp_msg += struct.pack('H', len(self._sensors_data))
            data_list = list()
            for one_data in list(self._sensors_data.values()):
                new_data = round(one_data, 2)
                data_list.append(new_data)
                tcp_msg += struct.pack('H', int(new_data * DATA_ZOOM))
            self._net_server.tcp.send_broadcast(tcp_msg)

            self.sign_sensors_data.emit(data_list)
            self.sign_sensor_data.emit(data_list[0], data_list[1], data_list[2])

            for sid in list(self._sensors_data.keys()):
                self._sensors_data[sid] = None

    def _event_cb(self, module, code, value):
        # print('event', module, code, value)
        if module == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (server_ip, server_port) = value
                self.sign_connection.emit(is_connected, server_ip, server_port)

    def _error_cb(self, module, code, value):
        # print('error', module, code, value)
        self.sign_server_error.emit(module, code, value)

    def _tcp_recv_cb(self, rx_msg, ip):
        # print('recv', rx_msg, ip)
        self.sign_server_recv.emit(rx_msg, ip)

    def launch(self):
        for one_sensor in list(self._sensors.values()):
            one_sensor.launch()

    def stop(self):
        for one_sensor in list(self._sensors.values()):
            one_sensor.stop()


if __name__ == '__main__':

    _pin_list = [1, 2, 3]
    sensor = UltraSonicLocal(_pin_list)
    sensor.launch()
    while 1:
        time.sleep(2)




