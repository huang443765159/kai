from PyQt5.QtWidgets import QMainWindow
from CARGUIDE.GUI.NUCGui.UI.UI import Ui_MainWindow
from CARGUIDE.DRIVER.GuideRemote.GuideRemote import GuideRemote


class NUCGui(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._nuc = GuideRemote()
        self._nuc.sign_data.connect(self._data)
        self._nuc.sign_error.connect(self._error)
        self._nuc.sign_event.connect(self._event)
        self.tcp_works.stateChanged.connect(self._set_tcp_launch)

    def _data(self, count, data_dict):
        self.data_log.append(f'[DATA] {count} {data_dict}')
        self.sensor_box1.setValue(list(data_dict.values())[0])
        self.sensor_box2.setValue(list(data_dict.values())[1])
        self.sensor_box3.setValue(list(data_dict.values())[2])

    def _error(self, error_type, code, value):
        self.event_log.append(f'[ERROR] {error_type} {code} {value}')

    def _event(self, event_type, code, value):
        if event_type == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (ip, port) = value
                self.tcp_connected_btn.setChecked(is_connected)
                self.tcp_ip_edit.setText(f'{ip}')
                self.tcp_port_edit.setText(f'{port}')
                self.tcp_type_edit.setText(f'{self._nuc.get_inviter_type()}')
        if event_type == 'ANET_INVITER':
            self.inviter_log.append(f'[INVITER]  <{code}> {value}')
        else:
            self.event_log.append(f'[EVENT]    <{event_type}> <{code}> {value}')

    def _set_tcp_launch(self, switch):
        # print(switch)
        if switch:
            self._nuc.launch()
        else:
            self._nuc.stop()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    _nuc = NUCGui()
    _nuc.show()

    sys.exit(app.exec_())
