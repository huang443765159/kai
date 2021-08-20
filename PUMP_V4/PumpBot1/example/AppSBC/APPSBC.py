import sys
sys.path.append('/home/pi/Desktop/')
import signal
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from PumpBot1.example.AppSBC.UI.UI import Ui_MainWindow
from PumpBot1.example.AppSBC._GuiSBC import GuiSBC
from PumpBot1.SBC.OnePump import OnePump

MACHINE_SN = 'TEST_1234'
BOT_ID = 1


class AppSBC(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.centralwidget.setFocus()
        QApplication.setStyle('Fusion')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # ON_TOP_WINDOW
        self._one_pump = OnePump(bot_id=BOT_ID, machine_sn=MACHINE_SN, config_dir='_config/Pump')
        # GUI
        self._gui = GuiSBC(ui=self._ui, one_pump=self._one_pump, bot_id=BOT_ID)
        # SIGNAL
        signal.signal(signal.SIGINT, self.closeEvent)

    def closeEvent(self, event_signum=None, frame=None):
        self._one_pump.exit()  # name


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    sbc = AppSBC()
    sbc.show()
    sys.exit(app.exec_())
