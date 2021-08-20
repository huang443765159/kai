import RPi.GPIO as GPIO
import threading
import time


class OneSensor(object):

    def __init__(self, sid, pin, cps, lock, data_cb):
        self._sid = sid
        self._pin = pin

        self._cps = cps
        self._lock = lock
        self._data_cb = data_cb

        self._thread = None
        self._thread_switch = False

    def _working(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        while self._thread_switch:
            self._lock.acquire()
            self._data_cb(sid=self._sid, data=int(GPIO.input(self._pin)))
            self._lock.release()
            time.sleep(1/self._cps)

    def launch(self):
        if self._thread_switch is False:
            self._thread_switch = True
            self._thread = threading.Thread(target=self._working)
            self._thread.start()

    def stop(self):
        if self._thread_switch:
            self._thread_switch = False


if __name__ == '__main__':
    pass
