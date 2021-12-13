import datetime
import threading
from PyQt5.QtCore import QObject, pyqtSignal


class _Relay(object):

    def open(self):
        pass

    def close(self):
        pass


class PumpSwitch(QObject):

    sign_pump_emit = pyqtSignal(int, str, bool)  # bot_id, instruct, is_open
    sign_pump_countdown = pyqtSignal(int, str, int)  # pump_id, instruct, countdown
    sign_pump_dev_online = None

    def __init__(self, bot_id):
        super().__init__()
        self._bot_id = bot_id
        # RELAYS
        self._relays = list()
        for i in range(16):
            _relay = _Relay()
            self._relays.append(_relay)
        # PUMP INSTRUCT
        self._pump_instruct = {'STOP_ALL': [relay for relay in self._relays],
                               'WHEEL': [self._relays[8], self._relays[0], self._relays[4]],
                               'CHEM_ALKALI': [self._relays[9], self._relays[1], self._relays[12]],
                               'CHEM_ACID': [self._relays[10], self._relays[2], self._relays[12]],
                               'WATER_WAX': [self._relays[11], self._relays[3], self._relays[12]],
                               'WATER_HIGH': [self._relays[13]], 'WATER_INFLOW': [self._relays[14]],
                               'DRAIN': [self._relays[15]]}

        # ATTR
        self._drain_switch = True
        self._turbo = 1
        # TIMER
        self._timer = dict()
        self._timer_switch = dict()
        self._ts = None
        self._t_end = None
        self._t_delay = dict()
        self._countdown = dict()

    def set_pump_emit(self, instruct, is_open, t_wait):
        if instruct in self._pump_instruct.keys():
            # SET IS_OPEN
            if is_open:
                t_wait = t_wait / self._turbo
                self._timer_switch[instruct] = True
                if instruct == 'DRAIN':
                    self._drain_start()
                if t_wait > self._countdown[instruct]:
                    self._countdown[instruct] = t_wait - self._countdown[instruct]
                    mode = 1
                else:
                    mode = 2
                    self._countdown[instruct] = self._countdown[instruct]
                    for _relay in self._pump_instruct[instruct]:
                        _relay.open()
                self._timer[instruct] = threading.Timer(self._countdown[instruct], lambda: self._timer_start(
                    mode=mode, instruct=instruct, is_open=is_open))
                self._timer[instruct].start()
            else:
                if instruct != 'STOP_ALL' and instruct in self._timer.keys() and self._timer[instruct].start:
                    self._timer[instruct].cancel()
                elif instruct == 'STOP_ALL':
                    for timer in self._timer.values():
                        if timer.start:
                            timer.cancel()
                self._timer_switch[instruct] = False
                for _relay in self._pump_instruct[instruct]:
                    _relay.close()
                self.sign_pump_emit.emit(self._bot_id, instruct, is_open)
            # SET COUNTDOWN
            if instruct not in ['DRAIN', 'WATER_INFLOW', 'STOP_ALL']:
                if is_open:
                    self._ts = datetime.datetime.now()
                else:
                    self._t_end = datetime.datetime.now()
                    if self._ts and self._t_end is not None:
                        t_duration = (self._t_end - self._ts).seconds
                        if t_duration < self._countdown[instruct]:
                            self._countdown[instruct] = self._countdown[instruct] - t_duration
                        else:
                            self._countdown[instruct] = self._t_delay[instruct]
                self.sign_pump_countdown.emit(self._bot_id, instruct, self._countdown[instruct])

    def _timer_start(self, mode, instruct, is_open):
        if self._timer_switch[instruct]:
            if mode == 2:
                self.sign_pump_emit.emit(self._bot_id, instruct, is_open)
            else:
                for _relay in self._pump_instruct[instruct]:
                    _relay.open()
                self.sign_pump_emit.emit(self._bot_id, instruct, is_open)

    def _drain_start(self):
        if self._drain_switch:
            self._drain_switch = False
            for relay in list(self._pump_instruct['DRAIN']):
                relay.open()
            print('开始排水')
            timer = threading.Timer(300, self._drain_close)
            timer.start()

    def _drain_close(self):
        for relay in list(self._pump_instruct['DRAIN']):
            relay.close()
        self._drain_switch = True
        print('停止排水')

    def load_ini(self, instruct, t_delay):
        self._t_delay[instruct] = t_delay / self._turbo
        self._countdown[instruct] = t_delay / self._turbo

    def get_t_delay(self):
        return self._t_delay

    def set_turbo(self, turbo):
        self._turbo = turbo

    def get_turbo(self):
        return self._turbo
