from PyQt5.QtCore import QObject, pyqtSignal
from INTERACTION1.DRIVER.Interaction.PumpsStation.Liquid._OneSensor import OneSensor

LIQUID_TYPE = {0: 'WATER', 1: 'ALKALI', 2: 'ACID', 3: 'WHEEL', 4: 'WAX'}


class Liquid(QObject):

    sign_data = pyqtSignal(dict)  # liquid_data

    def __init__(self, pi, rx_pins, tx_pins):
        super().__init__()
        # LIQUID
        self._liquid = dict()
        self._liquid_data = {'WATER': None, 'ALKALI': None, 'ACID': None, 'WHEEL': None, 'WAX': None}
        for sid, rx_pin in enumerate(rx_pins):
            self._liquid[LIQUID_TYPE[sid]] = OneSensor(pi=pi, sid=sid, rx_pin=rx_pin, tx_pin=tx_pins[sid], data_cb=self._data)

    def _data(self, sid, data):
        self._liquid_data[LIQUID_TYPE[sid]] = data
        if None not in self._liquid_data.values():
            print(self._liquid_data.copy())
            self.sign_data.emit(self._liquid_data.copy())
            for LIQUID_TYPE[sid] in self._liquid_data.keys():
                self._liquid_data[LIQUID_TYPE[sid]] = None


if __name__ == '__main__':
    import os
    import pigpio

    _pi = pigpio.pi()
    if not _pi.connected:
        os.system('sudo pigpiod')
        _pi = pigpio.pi()

    liquid = Liquid(pi=_pi, rx_pins=[15, 24, 8, 12, 20], tx_pins=[14, 23, 25, 7, 16])
    liquid.sign_data.connect(lambda x: print(x))
