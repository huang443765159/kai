import time
import threading
from PyQt5.QtCore import QObject, pyqtSignal


class OneSensor(object):

    def __init__(self, pin):
        self._pin = pin
        self._err = False
        try:
            import os
            import pigpio
            self._pi = pigpio.pi()
            if not self._pi.connected:
                os.system('sudo pigpiod')
                self._pi = pigpio.pi()
            self._pi.set_mode(pin, pigpio.INPUT)
            self._pi.set_pull_up_down(pin, pigpio.PUD_DOWN)
        except ImportError as err:
            self._err = True
            # print(err)

    def get_data(self):
        if not self._err:
            return bool(self._pi.read(self._pin))


class DrainSensors(QObject):

    sign_drain_ena_is_on = pyqtSignal(list)  # drain_ena_is_on_list

    def __init__(self, pins=(17, 18), sampling_frequency=0.1):
        super().__init__()
        # SENSORS
        self._sensors = dict()
        self._drain_is_ena_on = {0: False, 1: False}
        for sensor_id, pin in enumerate(pins):
            self._sensors[sensor_id] = OneSensor(pin=pin)
        # THREAD
        self._sampling_frequency = sampling_frequency
        self._thread = threading.Thread(target=self._working)
        self._thread_switch = True
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while self._thread_switch:
            for sensor_id in self._sensors.keys():
                one_drain_data = self._sensors[sensor_id].get_data()
                if self._drain_is_ena_on[sensor_id] != one_drain_data:
                    self._drain_is_ena_on[sensor_id] = one_drain_data
                    self.sign_drain_ena_is_on.emit(list(self._drain_is_ena_on.values()))
            time.sleep(self._sampling_frequency)

    def exit(self):
        self._thread_switch = False
