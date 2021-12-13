import signal
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from INTERACTIONS.AppNUC.UI.UI import Ui_MainWindow
from INTERACTIONS.AppNUC._GuiPumps import GuiPumps
from INTERACTIONS.AppNUC._GuiGuides import GuiGuides
from INTERACTIONS.NUC.Pumps.Pumps import Pumps
from INTERACTIONS.NUC.Guides.Guides import Guides

PUMP_MACHINE_SN = 'TEST_1234'
GUIDES_MACHINE_SN = 'TEST_1234'


class AppNuc(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.centralwidget.setFocus()
        QApplication.setStyle('Fusion')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # ON_TOP_WINDOW
        self._pumps = Pumps(machine_sn=PUMP_MACHINE_SN, config_dir='_config/Pump')
        self._guides = Guides(machine_sn=GUIDES_MACHINE_SN)
        # GUI
        self._gui_pumps = GuiPumps(ui=self._ui, pumps=self._pumps)
        self._gui_guides = GuiGuides(ui=self._ui, guides=self._guides)
        signal.signal(signal.SIGINT, self.closeEvent)

    def closeEvent(self, event_signum=None, frame=None):
        self._pumps.exit()
        self._guides.exit()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    nuc = AppNuc()
    nuc.show()
    sys.exit(app.exec_())
