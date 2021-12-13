# 192.168.50.191(办公室)
from PyQt5.QtWidgets import QMainWindow
from LEDDISPLAY.GUI.NucGui.UI.UI import Ui_MainWindow
from LEDDISPLAY.DRIVE.LedDisplayNuc.LedDisplayNuc import LedDisplay


class NucGui(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # LED DISPLAY
        self._led = LedDisplay()
        self._led.sign_error.connect(self._error)
        self._led.sign_connection.connect(self._connection)
        self._led.sign_display.connect(self._display)
        # BTN
        self.btn_welcome.clicked.connect(self._welcome)
        self.btn_forward.clicked.connect(self._forward)
        self.btn_stop.clicked.connect(self._stop)
        self.btn_back.clicked.connect(self._back)
        self.btn_wash_start.clicked.connect(self._wash_start)
        self.btn_wash_end.clicked.connect(self._wash_end)
        self.btn_tcp_works.stateChanged.connect(self._launch)

    def _error(self, error_type, code, error):
        self.error_log.append(f'[ERROR] {error_type} {code} {error}')

    def _connection(self, is_connected, ip, port):
        self.event_log.append(f'[CONNECTION] {is_connected} {ip} {port}')
        self.btn_connected.setChecked(is_connected)
        self.ip_edit.setText(f'{ip}')
        self.port_eidt.setText(f'{port}')
        self.type_edit.setText('LED DISPLAY')

    def _display(self, show, is_display):
        self.data_log.append(f'[DISPLAY] {show} {is_display}')

    def _welcome(self):
        self._led.send('WELCOME')

    def _forward(self):
        self._led.send('FORWARD')

    def _stop(self):
        self._led.send('STOP')

    def _back(self):
        self._led.send('BACK')

    def _wash_start(self):
        self._led.send('WASH START')

    def _wash_end(self):
        self._led.send('WASH END')

    def _launch(self, switch):
        self._led.launch() if switch else self._led.stop()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    gui = NucGui()
    gui.show()

    sys.exit(app.exec_())
