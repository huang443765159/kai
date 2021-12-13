import time
import threading
from PyQt5.QtCore import QObject, pyqtSignal, QTimer


class MathTiming(QObject):

    sign_pump_remain_ts = pyqtSignal(int, int, float, float)  # bot_id, liquid_id, remain_ts, extra_ts

    def __init__(self, bot_id, sampling_frequency=1):
        super().__init__()
        self._bot_id = bot_id
        self._sampling_frequency = sampling_frequency
        # ATTR
        self._remain_ts = dict()
        self._ts_to_jet = dict()
        self._remain_ts_memory = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
        self._liquid_switch = dict()
        for liquid_id in [0, 1, 2, 3, 4]:
            self._liquid_switch[liquid_id] = [False, 0]
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        QTimer.singleShot(100, lambda: self._thread.start())

    def _working(self):
        while 1:
            for liquid_id in self._liquid_switch.keys():
                if self._liquid_switch[liquid_id][0]:
                    self._remain_ts[liquid_id] = self._remain_ts[liquid_id] - self._sampling_frequency
                    if self._remain_ts[liquid_id] <= 0:
                        self._remain_ts[liquid_id] = 0
                else:
                    if self._remain_ts[liquid_id] == 0:
                        self._remain_ts[liquid_id] = self._ts_to_jet[liquid_id]
                    else:
                        self._remain_ts[liquid_id] = self._remain_ts[liquid_id]
                if self._remain_ts_memory[liquid_id] != self._remain_ts[liquid_id]:
                    self._remain_ts_memory[liquid_id] = self._remain_ts[liquid_id]
                    self.sign_pump_remain_ts.emit(
                        self._bot_id, liquid_id, self._remain_ts[liquid_id], self._liquid_switch[liquid_id][1])
            time.sleep(self._sampling_frequency)

    def sys_remain_ts_from_pump(self, remain_ts, ts_to_jet):
        self._remain_ts = remain_ts
        self._ts_to_jet = ts_to_jet

    def sys_pump_shooting_from_pump(self, liquid_id, switch, extra_ts):
        self._liquid_switch[liquid_id] = [switch, extra_ts]

    def stop_timing(self):
        for liquid_id in self._liquid_switch.keys():
            self._liquid_switch[liquid_id][0] = False
