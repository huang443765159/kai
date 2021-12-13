import signal
from PyQt5.QtWidgets import QMainWindow
from INTERACTIONS.AppNUC.UI.UI import Ui_MainWindow
from INTERACTIONS.AppNUC._GuiPumpStations import GuiPumpStations
from INTERACTIONS.AppNUC._GuiGuides import GuiGuides
from INTERACTIONS.NUC.PumpStations.PumpStations import  PumpStations
from INTERACTIONS.NUC.Guides.Guides import Guides

PUMP_MACHINE_SN = 'TEST_1234'
GUIDES_MACHINE_SN = 'TEST_1234'


class AppNuc(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._pump_stations = PumpStations(machine_sn=PUMP_MACHINE_SN, config_dir='_config/Pump')
        self._guides = Guides(machine_sn=GUIDES_MACHINE_SN)
        # GUI
        self._gui_pump_stations = GuiPumpStations(ui=self, pump_stations=self._pump_stations)
        self._gui_guides = GuiGuides(ui=self, guides=self._guides)
        signal.signal(signal.SIGINT, self.closeEvent)

    def closeEvent(self, event_signum=None, frame=None):
        self._pump_stations.exit()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    nuc = AppNuc()
    nuc.show()
    sys.exit(app.exec_())
