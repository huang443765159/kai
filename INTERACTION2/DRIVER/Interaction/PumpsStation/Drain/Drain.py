from PyQt5.QtCore import QObject, pyqtSignal
from INTERACTION2.DRIVER.Interaction.PumpsStation.Drain._OneSensor import OneSensor


class Drain(QObject):

    sign_data = pyqtSignal(list)  # drain_data

    def __init__(self, pi, pins):
        super().__init__()
        # DRAIN
        self._drain = dict()
        self._drain_data = {0: None, 1: None}
        self._drain_memory_data = dict()
        for sid, pin in enumerate(pins):
            self._drain[sid] = OneSensor(pi=pi, sid=sid, pin=pin, data_cb=self._data)

    def _data(self, sid, data):
        self._drain_data[sid] = data
        if None not in self._drain_data.values():
            # print('DRAIN', self._drain_data.copy())
            if self._drain_memory_data != self._drain_data.copy():
                self._drain_memory_data = self._drain_data.copy()
                self.sign_data.emit(list(self._drain_memory_data.values()))
            for sid in self._drain_data.keys():
                self._drain_data[sid] = None


if __name__ == '__main__':
    import os
    import pigpio

    _pi = pigpio.pi()
    if not _pi.connected:
        os.system('sudo pigpiod')
        _pi = pigpio.pi()

    drain = Drain(pi=_pi, pins=[17, 18])
    drain.sign_data.connect(lambda x: print(x))
