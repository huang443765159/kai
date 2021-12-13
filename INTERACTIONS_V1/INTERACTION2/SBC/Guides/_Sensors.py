import time
import threading
from PyQt5.QtCore import QObject, pyqtSignal


def import_pi_gpio(pin):
    import os
    import pigpio
    pi = pigpio.pi()
    if not pi.connected:
        os.system('sudo pigpiod')
        pi = pigpio.pi()
    pi.set_mode(pin, pigpio.INPUT)
    pi.set_pull_up_down(pin, pigpio.PUD_DOWN)
    return pi


class OneSensor(object):

    def __init__(self, pi_gpio, sid, pin, data_cb, sampling_frequency=0.1):
        if pi_gpio is not None:
            self._pi = import_pi_gpio(pin=pin)
            self._sid = sid
            self._pin = pin
            self._data_cb = data_cb
            # THREAD
            self._thread = threading.Thread(target=self._working)
            self._thread.daemon = True
            self._thread_switch = True
            self._thread.start()
            self._sampling_frequency = sampling_frequency

    def _working(self):
        while self._thread_switch:
            self._data_cb(sid=self._sid, data=bool(self._pi.read(self._pin)))
            time.sleep(self._sampling_frequency)

    def exit(self):
        self._thread_switch = False


class Sensors(QObject):

    sign_raw_data = pyqtSignal(list)  # raw_data

    def __init__(self, pins, pi_gpio):
        super().__init__()
        # SENSORS
        self._sensors = dict()
        self._row_data = {0: True, 1: True}
        for sid, pin in enumerate(pins):
            self._sensors[sid] = OneSensor(pi_gpio=pi_gpio, sid=sid, pin=pin, data_cb=self._data_callback)

    def _data_callback(self, sid, data):
        if self._row_data[sid] != data:
            self._row_data[sid] = data
            self.sign_raw_data.emit(list(self._row_data.values()))

    def exit(self):
        for guide in list(self._sensors.values()):
            guide.exit()
