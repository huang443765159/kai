import sys
# sys.path.append('/home/pi/Desktop/')
import signal
from PyQt5.QtWidgets import QMainWindow
from INTERACTION2.AppSBC.UI.UI import Ui_SBC
from INTERACTION2.AppSBC._GuiOnePumpStation import GuiOnePumpStation
from INTERACTION2.AppSBC._GuiGuides import GuiGuides
from INTERACTION2.SBC.OnePumpStation.OnePumpStation import OnePumpStation
from INTERACTION2.SBC.Guides.Guides import Guides

PUMP_MACHINE_SN = 'TEST_1234'
GUIDES_MACHINE_SN = 'TEST_1234'


class AppSBC(QMainWindow, Ui_SBC):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._one_pump_station = OnePumpStation(bot_id=2, machine_sn=PUMP_MACHINE_SN, config_dir='_config/Pump')
        self._guides = Guides(machine_sn=GUIDES_MACHINE_SN)
        # GUI
        self._gui_one_pump_station = GuiOnePumpStation(ui=self, one_pump_station=self._one_pump_station)
        self._gui_guides = GuiGuides(ui=self, guides=self._guides)
        # SIGNAL
        signal.signal(signal.SIGINT, self.closeEvent)

    def closeEvent(self, event_signum=None, frame=None):
        self._one_pump_station.exit()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    sbc = AppSBC()
    sbc.show()
    sys.exit(app.exec_())
