import os
import pigpio
from PyQt5.QtCore import QObject
from INTERACTION2.DRIVER.Interaction.Guides.Guides import Guides
from INTERACTION2.DRIVER.Interaction.PumpsStation.PumpsStation import PumpsStation


class Core(QObject):

    def __init__(self):
        super().__init__()
        # PI
        _pi = pigpio.pi()
        if not _pi.connected:
            os.system('sudo pigpiod')
            _pi = pigpio.pi()
        # DRIVER
        self.guides = Guides(pi=_pi, device_type='GUIDES', device_token='OPEN GUIDES')
        self.pumps_station = PumpsStation(pi=_pi, device_type='PUMPS STATION', device_token='OPEN PUMPS STATION')

    def exit(self):
        self.guides.exit()
        self.pumps_station.exit()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    core = Core()

    sys.exit(app.exec_())
