from PyQt5.QtWidgets import QMainWindow
from QTimer任务流模块.GUI.NucGUI.UI.UI import Ui_MainWindow
from QTimer任务流模块.DRIVER.WashSwitchNUC.WashSwitchNUC import WashSwitchNUC


class NucGUI(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # WASH
        self._wash = WashSwitchNUC()
        self._wash.sign_error.connect(self._error)
        self._wash.sign_connection.connect(self._connection)
        self._wash.sign_wash_type.connect(self._wash_type)
        # BTN
        self.btn_start.clicked.connect(lambda: self._wash.dance_start(switch=True))
        self.btn_tcp_works.stateChanged.connect(self._tcp_works)
        # TEST BTN
        self.btn_stop_all.clicked.connect(self._wash.all_stop)
        self.btn_wheel.stateChanged.connect(self._wash.wheel)
        self.btn_alkali_chem.stateChanged.connect(self._wash.alkali_chem)
        self.btn_high_water.stateChanged.connect(self._wash.high_water)
        self.btn_water_wax.stateChanged.connect(self._wash.water_wax)
        self.btn_acid_chem.stateChanged.connect(self._wash.acid_chem)

    def _error(self, error_type, code, error):
        self.error_log.append(f'<ERROR> {error_type} {code} {error}')

    def _connection(self, is_connected, ip, port):
        self.btn_connected.setChecked(is_connected)
        self.ip_edit.setText(f'{ip}')
        self.port_eidt.setText(f'{port}')
        self.type_edit.setText('WASH')

    def _wash_type(self, wash_type, switch):
        self.data_log.append(f'<DATA> {wash_type} {switch}')

    def _tcp_works(self, switch):
        self._wash.launch() if switch else self._wash.stop()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    _nuc = NucGUI()
    _nuc.show()

    sys.exit(app.exec_())
