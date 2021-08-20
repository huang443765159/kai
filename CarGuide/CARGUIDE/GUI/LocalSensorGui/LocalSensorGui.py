from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from CarGuide.CARGUIDE.GUI.LocalSensorGui.UI.UI import Ui_MainWindow
from CarGuide.CARGUIDE.DRIVER.LocalSensor.LocalSensor import LocalSensor


class LocalSensorGui(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self._local_sensor = LocalSensor([11, 16, 18])
        self._local_sensor.sign_sensors_data.connect(self._sensors_data)
        self._local_sensor.sign_sensor_data.connect(self._sensor_data)

        self._local_sensor.sign_tcp_event.connect(self._tcp_event)
        self._local_sensor.sign_tcp_error.connect(self._tcp_error)
        self._local_sensor.sign_tcp_recv.connect(self._tcp_recv)

    def _sensors_data(self, data_dict):
        self.sensors_data_log.append(f'{data_dict}')

    def _sensor_data(self, data1, data2, data3):
        self.sensor_box1.setValue(data1)
        self.sensor_box2.setValue(data2)
        self.sensor_box3.setValue(data3)
        self.sensor_state_edit1.setText('True') if data1 == 1 else self.sensor_state_edit1.setText('False')
        self.sensor_state_edit2.setText('True') if data2 == 1 else self.sensor_state_edit2.setText('False')
        self.sensor_state_edit3.setText('True') if data3 == 1 else self.sensor_state_edit3.setText('False')

    def _tcp_event(self, is_connected, ip, port):
        self.tcp_event_log.append(f'{is_connected} {ip} {port}')
        self.tcp_connected_btn.setChecked(is_connected)
        self.tcp_ip_edit.setText(f'{ip}')
        self.tcp_port_edit.setText(f'{port}')
        self.tcp_type_edit.setText('Sensor')

    def _tcp_error(self, module, code, value):
        self.tcp_error_log.append(f'{module} {code} {value}')

    def _tcp_recv(self, rx_msg, ip):
        self.tcp_recv_log.append(f'{rx_msg} {ip}')

    @pyqtSlot()
    def on_sensor_start_btn_clicked(self):
        self._local_sensor.thread_launch()

    @pyqtSlot()
    def on_sensor_stop_btn_clicked(self):
        self._local_sensor.thread_stop()


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    local_sensor = LocalSensorGui()
    local_sensor.show()

    sys.exit(app.exec_())
