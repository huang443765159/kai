from PyQt5.QtCore import QObject
from INTERACTIONS.DRIVER.Interactions.Guides.Guides import Guides
from INTERACTIONS.DRIVER.Interactions.PumpsStation.PumpsStation import PumpsStation


class Core(QObject):

    def __init__(self):
        super().__init__()
        # DRIVE
        self.guides = Guides(device_type='GUIDES', device_token='OPEN GUIDES')
        self.pumps_station = dict()
        for device_id in [1, 2]:
            self.pumps_station[device_id] = PumpsStation(device_id=device_id, device_type='PUMP STATION', device_token='OPEN PUMP STATION')

    def exit(self):
        self.guides.exit()
        for device_id in [1, 2]:
            self.pumps_station[device_id].exit()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    _core = Core()

    sys.exit(app.exec_())
