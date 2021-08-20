# import RPi.GPIO as GPIO
import threading
import random
import signal
import time
import sys


class OneSensor(object):

    def __init__(self, sid, pin, lock, data_cb):

        self._sid = sid
        self._pin = pin
        self._lock = lock
        self._data_cb = data_cb

        self._thread = None
        self._thread_switch = False

        signal.signal(signal.SIGINT, self._sys_quit)

    def _working(self):
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        while self._thread_switch:
            self._lock.acquire()
            self._data_cb(sid=self._sid, data=random.randint(0, 1))
            # if GPIO.input(self._pin):
            #     self._data_cb(sid=self._sid, data=1)
            # else:
            #     self._data_cb(sid=self._sid, data=0)
            self._lock.release()
            time.sleep(1 / 8)

    def launch(self):
        if self._thread_switch is False:
            self._thread_switch = True

            self._thread = threading.Thread(target=self._working)
            self._thread.daemon = True
            self._thread.start()

    def stop(self):
        if self._thread_switch:
            self._thread_switch = False

    @staticmethod
    def _sys_quit(signal_num, handler):
        print('SYS QUIT')
        sys.exit(0)
