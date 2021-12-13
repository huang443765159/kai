import threading
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from INTERACTIONS.NUC.Pumps._MathTiming import MathTiming


LIQUID_WATER_HIGH = 0
LIQUID_CH_A = 1
LIQUID_CH_B = 2
LIQUID_CH_WHL = 3
LIQUID_CH_WAX = 4


class MathOnePump(QObject):

    sign_pump_shooting = pyqtSignal(int, int, bool)  # bot_id, liquid_id, switch
    sign_pump_remain_ts = pyqtSignal(int, int, float, float)  # bot_id, liquid_id, remain_ts, extra_ts

    def __init__(self, bot_id, config_dir):
        super().__init__()
        self._bot_id = bot_id
        self._config_dir = config_dir
        # RELAYS
        self._liquid_types = dict()
        for i in range(17):
            self._liquid_types[i] = i
        # ATTR
        self._turbo = 1
        self._link = False
        # TIMER
        self._timer = dict()  # PY_TIMER
        self._ts_to_jet = dict()
        self._ts_remain = dict()
        QTimer.singleShot(300, self._timing_init)

    def _timing_init(self):
        self._math_timing = MathTiming(bot_id=self._bot_id)
        self.sys_remain_ts_to_timing()
        self._math_timing.sign_pump_remain_ts.connect(self.sign_pump_remain_ts)

    # FUNC
    def set_pump_shooting(self, liquid_id, switch, extra_ts):
        if not self._link:
            if liquid_id in self._liquid_types.keys():
                if switch:
                    # PUMP OPEN
                    self._ts_remain[liquid_id] = (self._ts_remain[liquid_id] + extra_ts) / self._turbo
                    self.sys_remain_ts_to_timing()
                    self._timer[liquid_id] = threading.Timer(
                        self._ts_remain[liquid_id],
                        lambda: self.sign_pump_shooting.emit(self._bot_id, liquid_id, switch))
                    self._timer[liquid_id].start()
                else:
                    # PUMP CLOSE
                    if liquid_id in self._timer.keys() and self._timer[liquid_id].start:
                        self._timer[liquid_id].cancel()
                    self.sign_pump_shooting.emit(self._bot_id, liquid_id, switch)
                self._math_timing.sys_pump_shooting_from_pump(liquid_id, switch, extra_ts)
            else:
                print(f'\033[1;33m [LIQUID_TYPE_ERR] {liquid_id} \033[0m')

    def stop_all(self):
        for timer in self._timer.values():
            timer.cancel()
        self._math_timing.stop_timing()

    # STATE
    def get_pump_remain_ts(self, liquid_id):
        return self._ts_remain[liquid_id]

    def set_ts_to_jet(self, liquid_id, ts_remain):
        self._ts_remain[liquid_id] = ts_remain
        self._ts_to_jet[liquid_id] = ts_remain

    def get_ts_to_jet(self, liquid_id):
        return self._ts_to_jet[liquid_id]

    def set_link(self, link: bool):
        self._link = link

    def get_link(self):
        return self._link

    def set_turbo(self, turbo=1):
        self._turbo = turbo

    def get_turbo(self):
        return self._turbo

    def sys_remain_ts_to_timing(self):
        self._math_timing.sys_remain_ts_from_pump(self._ts_remain, self._ts_to_jet)
