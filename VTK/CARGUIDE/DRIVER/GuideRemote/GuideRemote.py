import struct
from PyQt5.QtCore import QObject, pyqtSignal
from CARGUIDE.DRIVER.AutoNET.NetClient import NetClient


class GuideRemote(QObject):

    sign_data = pyqtSignal(int, dict)  # count ,data_dict

    sign_event = pyqtSignal(str, str, tuple)  # event_type, code, value
    sign_error = pyqtSignal(str, str, object)  # error_type, code, value

    def __init__(self, port=8888, inviter_type='Guide', inviter_id=0):
        super().__init__()
        self._port = port
        self._sensor_num = 0
        self._tcp_recv_count = 0
        self._inviter_id = inviter_id
        self._inviter_type = inviter_type
        self._network = NetClient(event_cb=self._event,
                                  error_cb=self._error,
                                  tcp_recv_cb=self._tcp_recv,
                                  tcp_port=self._port,
                                  invite_type=self._inviter_type,
                                  invite_id=self._inviter_id)
        self.get_my_id = self._network.get_my_ip
        self.get_server_ip = self._network.get_server_ip
        self.get_server_port = self._network.get_server_port
        self.launch = self._network.launch
        self.stop = self._network.stop

    def _event(self, module, code, value):
        self.sign_event.emit(module, code, value)

    def _error(self, module, code, value):
        self.sign_error.emit(module, code, value)

    def _tcp_recv(self, rx_msg, ip):
        self._sensor_num = struct.unpack('H', rx_msg[0:2])[0]
        data = dict()
        for i in range(1, self._sensor_num+1):
            sensor_data = struct.unpack('H', rx_msg[i*2:2+i*2])[0]
            data[i-1] = sensor_data
        self._tcp_recv_count += 1
        self.sign_data.emit(self._tcp_recv_count, data)

    def is_connected(self):
        return self._network.tcp.is_connected()

    def get_sensor_num(self):
        if self.is_connected():
            sensor_num = self._sensor_num
        else:
            sensor_num = 0
        return sensor_num

    def get_inviter_type(self):
        return self._inviter_type

    def get_inviter_id(self):
        return self._inviter_id


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    guide_remote = GuideRemote()
    guide_remote.sign_data.connect(lambda x: print('GuideWork', x))
    guide_remote.sign_error.connect(lambda x, y, z: print('ERROR', x, y, z))
    guide_remote.sign_event.connect(lambda x, y, z: print('EVENT', x, y, z))

    sys.exit(app.exec_())
