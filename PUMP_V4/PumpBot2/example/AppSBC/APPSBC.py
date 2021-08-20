import sys
sys.path.append('/home/pi/Desktop/')
import signal
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from PumpBot2.example.AppSBC.UI.UI import Ui_MainWindow
from PumpBot2.example.AppSBC._GuiOnePump import GuiOnePump
from PumpBot2.example.AppSBC._GuiGuides import GuiGuides
from PumpBot2.SBC.Guides.Guides import Guides
from PumpBot2.SBC.OnePump.OnePump import OnePump

MACHINE_SN = 'TEST_1234'
BOT_ID = 2


class AppSBC(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.centralwidget.setFocus()
        QApplication.setStyle('Fusion')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # ON_TOP_WINDOW
        self._one_pump = OnePump(bot_id=BOT_ID, machine_sn=MACHINE_SN, config_dir='_config/Pump')
        self._guides = Guides(machine_sn=MACHINE_SN)
        # GUI
        self._gui_one_pump = GuiOnePump(ui=self._ui, one_pump=self._one_pump, bot_id=BOT_ID)
        self._gui_guides = GuiGuides(ui=self._ui, guides=self._guides)
        # SIGNAL
        signal.signal(signal.SIGINT, self.closeEvent)

    def closeEvent(self, event_signum=None, frame=None):
        self._one_pump.exit()
        self._guides.exit()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    sbc = AppSBC()
    sbc.show()
    sys.exit(app.exec_())
