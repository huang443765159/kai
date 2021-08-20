import time
import threading


class VirtualDance(object):

    def __init__(self, event_cb):
        super().__init__()
        # CALLBACK
        self._event_cb = event_cb
        # ATTR
        self._ts_start = 0
        self._ts_stop = 0
        self._switch = False
        self._wash_type = None
        self._ts_duration = 0
        # THREAD
        self._thread = None
        self._switch = False

    def _working(self):
        while self._switch:
            self._ts_stop = time.time()
            if self._ts_stop - self._ts_start >= self._ts_duration:  # 模拟持续时间
                self._switch = False  # 模拟停止
                self._event_cb(wash_type=self._wash_type, switch=self._switch)
            time.sleep(0.02)

    def start(self, wash_type, ts_duration):
        self._switch = True
        self._wash_type = wash_type
        self._ts_duration = ts_duration
        self._ts_start = time.time()
        self._event_cb(wash_type=self._wash_type, switch=self._switch)
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def stop(self, switch):
        self._switch = switch
