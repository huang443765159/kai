import os
import time
import pigpio
import threading


class Test(object):

    def __init__(self, pin, data_cb):
        self._pin = pin
        self._data_cb = data_cb
        # PI
        self._pi = pigpio.pi()
        if not self._pi.connected:
            os.system('sudo pigpiod')
            time.sleep(1)
            self._pi = pigpio.pi()
        self._pi.set_mode(self._pin, pigpio.INPUT)
        self._pi.set_pull_up_down(self._pin, pigpio.PUD_DOWN)
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            self._data_cb(data=self._pi.read(bool(self._pin)))
            time.sleep(1)


if __name__ == '__main__':

    def _data_cb(data):
        print(data)

    test = Test(pin=18, data_cb=_data_cb)
    while 1:
        time.sleep(1)