import signal
from PyQt5.QtWidgets import QMainWindow
from INTERACTION1.AppSBC.UI.UI import Ui_SBC
from INTERACTION1.AppSBC._GuiSBC import GuiSBC
from INTERACTION1.SBC.OnePumpStation import OnePumpStation

MACHINE_SN = '55334422'


class AppSBC(QMainWindow, Ui_SBC):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._one_pump_station = OnePumpStation(device_id=1, machine_sn=MACHINE_SN)
        # GUI
        self._gui = GuiSBC(ui=self, one_pump_station=self._one_pump_station)
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
