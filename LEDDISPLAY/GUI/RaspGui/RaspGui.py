from PyQt5.QtWidgets import QMainWindow
from LEDDISPLAY.GUI.RaspGui.UI.UI import Ui_MainWindow
from LEDDISPLAY.DRIVE.AutoNET.NetInviter import NetInviter
from LEDDISPLAY.DRIVE.LedDispalayRasp.LedDisplayRasp import LedDisplay


class RaspGui(QMainWindow, Ui_MainWindow):

    def __init__(self, invite_type='LED DISPLAY', invite_id=1):
        super().__init__()
        self.setupUi(self)
        # INVITER
        self._inviter = NetInviter(invite_type=invite_type, invite_id=invite_id)
        # LED DISPLAY
        self._led = LedDisplay(pins=[35, 36, 37, 38, 40])
        # SIGNAL
        self._led.sign_error.connect(self._error)
        self._led.sign_connection.connect(self._connection)
        self._led.sign_display.connect(self._display)
        # BTN
        self.btn_stop.clicked.connect(self._stop)
        self.btn_welcome.clicked.connect(self._welcome)
        self.btn_back.clicked.connect(self._back)
        self.btn_forward.clicked.connect(self._forward)
        self.btn_wash_start.clicked.connect(self._wash_start)
        self.btn_wash_end.clicked.connect(self._wash_end)

    def _stop(self):
        self._led.set_display(show='STOP')

    def _welcome(self):
        self._led.set_display(show='WELCOME')

    def _back(self):
        self._led.set_display(show='BACK')

    def _forward(self):
        self._led.set_display(show='FORWARD')

    def _wash_start(self):
        self._led.set_display(show='WASH START')

    def _wash_end(self):
        self._led.set_display(show='WASH END')

    def _error(self, error_type, code, error):
        self.error_log.append(f'[ERROR] {error_type} {code} {error}')

    def _connection(self, is_connected, ip, port):
        self.event_log.append(f'[CONNECTION] {is_connected} {ip} {port}')
        self.btn_connected.setChecked(is_connected)
        self.ip_edit.setText(f'{ip}')
        self.port_eidt.setText(f'{port}')
        self.type_edit.setText('LED DISPLAY')

    def _display(self, show, is_display):
        self.data_log.append(f'{show} {is_display}')


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    gui = RaspGui()
    gui.show()

    sys.exit(app.exec_())
