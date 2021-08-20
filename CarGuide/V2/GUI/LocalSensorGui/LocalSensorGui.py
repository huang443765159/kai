from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from V2.GUI.LocalSensorGui.UI.UI import Ui_MainWindow
from V2.DRIVER.LocalSensor.LocalSensor import LocalSensor


class LocalSensorGui(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._local_sensor = LocalSensor([1, 2, 3])
        self._local_sensor.sign_sensors_data.connect(self._sensors_data)
        self._local_sensor.sign_sensor_data.connect(self._sensor_data)
        self._local_sensor.sign_connect.connect(self._connection)
        self._local_sensor.sign_error.connect(self._error)
        self._local_sensor.sign_recv.connect(self._recv)

        self._count = 0

    def _sensors_data(self, data_dict):
        new_data_dict = dict()
        self.sensor_data_log.append(f'{data_dict}')
        if new_data_dict != data_dict:
            self._count += 1
        self.sensor_stand.setText(f'{self._count}')

    def _sensor_data(self, data1, data2, data3):
        self.sensor_box1.setValue(data1)
        self.sensor_box2.setValue(data2)
        self.sensor_box3.setValue(data3)

    def _connection(self, is_connected, ip, port):
        self.tcp_connect_btn.setChecked(is_connected)
        self.ip_edit.setText(f'{ip}')
        self.port_edit.setText(f'{port}')
        self.type_edit.setText('Sensor')

    def _error(self, module, code, value):
        self.error_log.setText(f'{module} {code} {value}')

    def _recv(self, rx_msg, ip):
        self.recv_log.setText(f'{rx_msg} {ip}')

    @pyqtSlot()
    def on_sensor_btn_start_clicked(self):
        self._local_sensor.launch()

    @pyqtSlot()
    def on_sensor_stop_btn_clicked(self):
        self._local_sensor.stop()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    local_gui = LocalSensorGui()
    local_gui.show()

    sys.exit(app.exec_())

