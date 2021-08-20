from PyQt5.Qt import QTimer


def _ts_remain_timer_start(self, liquid_id, switch=False, extra_ts=0):
    self._remain_ts_timer[liquid_id] = QTimer()
    self._remain_ts_timer[liquid_id].start(1000)
    self._remain_ts_timer[liquid_id].timeout.connect(lambda: self._cal_remain_ts(liquid_id, switch, extra_ts))


def _cal_remain_ts(self, liquid_id, switch, extra_ts=0):
    ts_remain_copy = self._ts_remain[liquid_id]
    if switch:
        print(1, switch)
        self._ts_remain[liquid_id] = self._ts_remain[liquid_id] - 1
        if self._ts_remain[liquid_id] <= 0:
            self._ts_remain[liquid_id] = 0
    else:
        print(2, switch)
        if self._ts_remain[liquid_id] == 0:
            self._ts_remain[liquid_id] = self._ts_delay[liquid_id]
        else:
            self._ts_remain[liquid_id] = self._ts_remain[liquid_id]
    if ts_remain_copy != self._ts_remain[liquid_id]:
        self.sign_pump_remain_ts.emit(self._bot_id, liquid_id, self._ts_remain[liquid_id], extra_ts)
        print(3)
