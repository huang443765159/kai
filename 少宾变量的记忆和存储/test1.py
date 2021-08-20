import threading
import time
import random


class OneSensor(object):

    def __init__(self, sid, pin, data_cb):
        self._sid = sid
        self._pin = pin
        self._data_cb = data_cb

        self._thread = None
        self._thread_switch = False

    def _working(self):
        while self._thread_switch:
            self._data_cb(sid=self._sid, data=random.randint(0, 100))
            # self._data_cb(sid=self._sid, data=0)
            time.sleep(1)

    def launch(self):
        if self._thread_switch is False:
            self._thread = threading.Thread(target=self._working)
            self._thread.daemon = True
            self._thread_switch = True
            self._thread.start()

    def stop(self):
        if self._thread_switch:
            self._thread_switch = False
            self._thread.join()


if __name__ == '__main__':

    while 1:
        time.sleep(1)
