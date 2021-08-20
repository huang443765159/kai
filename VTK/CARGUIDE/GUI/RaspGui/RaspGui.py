from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from CARGUIDE.GUI.RaspGui.UI.UI import Ui_MainWindow
from CARGUIDE.DRIVER.AutoNET.NetInviter import NetInviter
from CARGUIDE.DRIVER.GuideLocal.GuideLocal import GuideLocal


class RaspGui(QMainWindow, Ui_MainWindow):

    sign_event_thread_safe = pyqtSignal(str, str, tuple)  # event_type, code, value

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sign_event_thread_safe.connect(self._event)
        self._local = GuideLocal(pin_list=[11, 16, 18])
        self._local.sign_data.connect(self._data)
        self._local.sign_error.connect(self._error)
        self._local.sign_event.connect(self._event_thread_safe)
        self._inviter = NetInviter(invite_type='Guide', invite_id=0, event_cb=self._event_thread_safe)
        self.inviter_works.stateChanged.connect(self._set_inviter_launch)

    def _event_thread_safe(self, module, code, value):
        self.sign_event_thread_safe.emit(module, code, value)

    def _data(self, count, data_dict):
        self.data_log.append(f'[DATA] {count} {data_dict}')
        self.sensor_box1.setValue(list(data_dict.values())[0])
        self.sensor_box2.setValue(list(data_dict.values())[1])
        self.sensor_box3.setValue(list(data_dict.values())[2])

    def _error(self, error_type, code, error):
        self.event_log.append(f'[ERROR] {error_type} {code} {error}')

    def _event(self, event_type, code, value):
        if event_type == 'ANET_TCP':
            if code == 'CONNECT':
                is_connected, (ip, port) = value
                self.tcp_connected_btn.setChecked(is_connected)
                self.tcp_ip_edit.setText(f'{ip}')
                self.tcp_port_edit.setText(f'{port}')
                self.tcp_type_edit.setText('Guide')
        if event_type == 'ANET_INVITER':
            self.inviter_log.append(f'[INVITER] <{code}> {value}')
        else:
            self.event_log.append(f'[EVENT] <{event_type}> <{code}> {value}')

    def _set_inviter_launch(self, switch):
        if switch:
            self._inviter.launch()
        else:
            self._inviter.stop()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    local = RaspGui()
    local.show()

    sys.exit(app.exec_())
