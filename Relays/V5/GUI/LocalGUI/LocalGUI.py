from PyQt5.QtWidgets import QMainWindow
from QTimer任务流模块.GUI.LocalGUI.UI.UI import Ui_MainWindow
from QTimer任务流模块.DRIVER.AutoNET.NetInviter import NetInviter
from QTimer任务流模块.DRIVER.WashSwitchLocal.WashSwitchLocal import WashSwitchLocal


class LocalGUI(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # WASH
        self._wash = WashSwitchLocal(relays_ip=[0x10, 0x11, 0x12], relays_addr=[1, 2, 3, 4])
        # SIGNAL
        self._wash.sign_error.connect(self._error)
        self._wash.sign_wash_type.connect(self._wash_type)
        self._wash.sign_connection.connect(self._connection)
        # NETWORK
        self._network = NetInviter(invite_type='WASH', invite_id=1)
        # BTN
        self.btn_start.clicked.connect(self._wash_sys_start)
        self.btn_inviter.stateChanged.connect(self._inviter_lunch)
        # TEST BTN
        self.btn_stop_all.clicked.connect(self._wash.stop)
        self.btn_wheel.stateChanged.connect(self._wash.wheel)
        self.btn_alkali_chem.stateChanged.connect(self._wash.alkali_chem)
        self.btn_high_water.stateChanged.connect(self._wash.high_water)
        self.btn_water_wax.stateChanged.connect(self._wash.water_wax)
        self.btn_acid_chem.stateChanged.connect(self._wash.acid_chem)

    def _wash_sys_start(self):
        self._wash.dance_start(wash_type='ALKALI CHEM')

    def _error(self, error_type, code, error):
        self.error_log.append(f'<ERROR> {error_type} {code} {error}')

    def _connection(self, is_connected, ip, port):
        self.btn_connected.setChecked(is_connected)
        self.ip_edit.setText(f'{ip}')
        self.port_eidt.setText(f'{port}')
        self.type_edit.setText('WASH')

    def _wash_type(self, wash_type, switch):
        self.data_log.append(f'<DATA> {wash_type} {switch}')

    def _inviter_lunch(self, switch):
        self._network.launch() if switch else self._network.stop()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    local = LocalGUI()
    local.show()

    sys.exit(app.exec_())
