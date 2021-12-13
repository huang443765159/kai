import time
import pigpio
import threading


class OneSensor(object):

    def __init__(self, pi, sid, pin, data_cb):
        self._pi = pi
        self._sid = sid
        self._pin = pin
        self._data_cb = data_cb
        # PI
        self._pi.set_mode(self._pin, pigpio.INPUT)
        self._pi.set_pull_up_down(self._pin, pigpio.PUD_DOWN)
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            self._data_cb(sid=self._sid, data=bool(self._pi.read(self._pin)))
            time.sleep(0.1)


if __name__ == '__main__':
    import os

    _pi = pigpio.pi()
    if not _pi.connected:
        os.system('sudo pigpiod')
        _pi = pigpio.pi()

    def _data_cb(sid, data):
        print(sid, data)

    sensor = OneSensor(pi=_pi, sid=1, pin=21, data_cb=_data_cb)
