import time
import threading
from PyQt5.QtCore import QObject, pyqtSignal

LIQUID_TYPE = {0: 'WATER', 1: 'ALKALI', 2: 'ACID', 3: 'WHEEL', 4: 'WAX'}


def import_pi_gpio(rx_pin, tx_pin, baud=9600):
    import pigpio
    pi = pigpio.pi()
    pi.set_mode(rx_pin, pigpio.INPUT)
    pi.set_mode(tx_pin, pigpio.OUTPUT)
    pigpio.exceptions = False
    pi.bb_serial_read_close(rx_pin)
    pigpio.exceptions = True
    pi.bb_serial_read_open(rx_pin, baud, 8)
    return pi


class OneSensor(object):

    def __init__(self, pi_gpio, sid, rx_pin, tx_pin, data_cb, sampling_frequency=1):
        if pi_gpio is not None:
            self._pi = import_pi_gpio(rx_pin=rx_pin, tx_pin=tx_pin)
            self._sid = sid
            self._rx_pin = rx_pin
            self._data_cb = data_cb
            self._raw_msg = bytes()
            # THREAD
            self._thread = threading.Thread(target=self._working)
            self._thread.daemon = True
            self._thread_switch = True
            self._thread.start()
            self._sampling_frequency = sampling_frequency

    def _working(self):
        while self._thread_switch:
            count, data = self._pi.bb_serial_read(self._rx_pin)
            if count:
                self._raw_msg += data
                if len(self._raw_msg) == 4:
                    if (self._raw_msg[0] + self._raw_msg[1] + self._raw_msg[2]) & 0x00ff == self._raw_msg[3]:
                        self._data_cb(sid=self._sid, data=self._raw_msg[1] * 256 + self._raw_msg[2])
                self._raw_msg = bytes()
            # self._data_cb(sid=self._sid, data=random.randint(100, 200))
            time.sleep(self._sampling_frequency)

    def exit(self):
        self._thread_switch = False


class Liquid(QObject):

    sign_liquid_raw_data = pyqtSignal(dict)  # liquid_raw_data

    def __init__(self, pi_gpio, rx_pins=(14, 23, 25, 7, 16), tx_pins=(15, 24, 8, 12, 20)):
        super().__init__()
        # LIQUID
        self._liquid = dict()
        self._liquid_raw_data = {'WATER': 0, 'ALKALI': 0, 'ACID': 0, 'WHEEL': 0, 'WAX': 0}
        for sid, rx_pin in enumerate(rx_pins):
            self._liquid[LIQUID_TYPE[sid]] = OneSensor(pi_gpio=pi_gpio, sid=sid, rx_pin=rx_pin,
                                                       tx_pin=tx_pins[sid], data_cb=self._data_callback)

    def _data_callback(self, sid, data):
        self._liquid_raw_data[LIQUID_TYPE[sid]] = data
        self.sign_liquid_raw_data.emit(self._liquid_raw_data)

    def exit(self):
        for liquid in list(self._liquid.values()):
            liquid.exit()
