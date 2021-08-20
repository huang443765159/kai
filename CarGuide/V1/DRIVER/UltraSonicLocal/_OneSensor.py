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
            self._data_cb(sid=self._sid, data=random.random())
            time.sleep(0.1)

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

    def _data_cb(sid, data):
        print(f'{sid} {data}')

    one_sensor = OneSensor(sid=1, pin=2, data_cb=_data_cb)
    two_sensor = OneSensor(sid=2, pin=3, data_cb=_data_cb)
    one_sensor.launch()
    two_sensor.launch()
    while 1:
        time.sleep(1)


