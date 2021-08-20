from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from CarGuide.V1.GUI.LOCAL.UI.UI import Ui_MainWindow
from CarGuide.V1.DRIVER.UltraSonicLocal.UltraSonicLocal import UltraSonicLocal


class GuiSensorServer(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._sensor = UltraSonicLocal([1, 2, 3])

        self._sensor.sign_sensors_data.connect(self._sensors_data)
        self._sensor.sign_sensor_data.connect(self._sensor_data)

        self._sensor.sign_server_recv.connect(self._recv)
        self._sensor.sign_server_error.connect(self._error)
        self._sensor.sign_connection.connect(self._connection)
        self._sensor_count = 0
        self._sensor_data_list = None

    def _recv(self, rx_msg, ip):
        self.recv_log.append(f'<RX> {rx_msg} {ip}')

    def _error(self, module, code, value):
        self.error_log.append(f'<ERROR> {module} {code} {value}')

    def _connection(self, is_connected, peer_ip, peer_port):
        self.tcp_connect_btn.setChecked(is_connected)
        self.ip_edit.setText(f'{peer_ip}')
        self.port_edit.setText(f'{peer_port}')

    def _sensors_data(self, data_list):
        # print(data)
        self.sensor_data_log.append(f'{data_list}')
        if self._sensor_data_list != data_list:
            self._sensor_count += 1
        self.sensor_stand.setText(f'{self._sensor_count}')

    def _sensor_data(self, data1, data2, data3):
        # print(data1, data2, data3)
        self.sensor_box1.setValue(data1)
        self.sensor_box2.setValue(data2)
        self.sensor_box3.setValue(data3)

    @pyqtSlot()
    def on_sensor_btn_start_clicked(self):
        self._sensor.launch()

    @pyqtSlot()
    def on_sensor_stop_btn_clicked(self):
        self._sensor.stop()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    _server = GuiSensorServer()
    _server.show()

    sys.exit(app.exec_())

