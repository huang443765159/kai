import sys
import signal
import struct
import threading
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from CARGUIDE.DRIVER.AutoNET.NetServer import NetServer
from CARGUIDE.DRIVER.GuideLocal._OneSensor import OneSensor


class GuideLocal(QObject):

    sign_data = pyqtSignal(int, dict)  # count, data_dict

    sign_event = pyqtSignal(str, str, tuple)  # event_type, code, value
    sign_error = pyqtSignal(str, str, object)  # error_type, code, error

    def __init__(self, pin_list, cps=20, port=8888):
        super().__init__()
        self._lock = threading.Lock()
        self._tcp_send_count = 0
        self._sensors = dict()
        self._data = {0: None, 1: None, 2: None}
        self._new_data = dict()
        self._memory_data = dict()
        for sid, pin in enumerate(pin_list):
            self._sensors[sid] = OneSensor(sid=sid, pin=pin, cps=cps, data_cb=self._data_cb, lock=self._lock)

        self._network = NetServer(event_cb=self._connection, error_cb=self._error,
                                  tcp_recv_cb=self._tcp_recv, tcp_port=port)
        self.get_my_ip = self._network.tcp.get_my_ip
        self.connected = self._network.tcp.is_connected
        self.get_server_port = self._network.get_server_port
        self.get_client_ips = self._network.tcp.get_client_ips

        signal.signal(signal.SIGINT, self._sys_quit)
        for sensor in self._sensors.values():
            sensor.launch()
        QTimer().start(200)

    def _data_cb(self, sid, data):
        self._data[sid] = data
        if None not in self._data.values():
            self._new_data = self._data.copy()
            for sid in self._data.keys():
                self._data[sid] = None
        if self._memory_data != self._new_data:
            self._memory_data = self._new_data
            self.sign_data.emit(self._tcp_send_count, self._new_data)
            self._tcp_send_count += 1
            msg = struct.pack('H', len(self._new_data))
            for sensor_data in self._new_data.values():
                msg += struct.pack('H', sensor_data)
            self._network.tcp.send_broadcast(msg)

    def _connection(self, module, code, value):
        self.sign_event.emit(module, code, value)

    def _error(self, module, code, value):
        self.sign_error.emit(module, code, value)

    def _tcp_recv(self, module, code, value):
        pass

    @staticmethod
    def _sys_quit(signal_num=None, handler=None):
        print('SYS QUIT')
        sys.exit(0)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    guide_local = GuideLocal(pin_list=[11, 16, 18])
    guide_local.sign_data.connect(lambda x, data_dict: print('GuideWork', x, data_dict))
    guide_local.sign_event.connect(lambda x, y, z: print(f'TCP{x} {y} {z}'))
    guide_local.sign_error.connect(lambda module, code, value: print(f'ERROR {module} {code} {value}'))

    sys.exit(app.exec_())
