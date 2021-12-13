import time
import smbus
import threading
from PyQt5.QtCore import QObject, pyqtSignal


class _Relay(object):

    def __init__(self, dev_addr, slave_addr):
        self._dev_addr = dev_addr
        self._slave_addr = slave_addr
        # BUS
        self._bus = smbus.SMBus(1)

    def open(self):
        self._bus.write_byte_data(self._dev_addr, self._slave_addr, 0xff)

    def close(self):
        self._bus.write_byte_data(self._dev_addr, self._slave_addr, 0x00)


class GuidesDisplay(QObject):

    sign_display_show = pyqtSignal(str)  # display show

    def __init__(self, dev_addr, slave_addrs):
        super().__init__()
        self._dev_addr = dev_addr
        self._slave_addrs = slave_addrs
        # RELAYS
        self._relays = list()
        for slave_addr in slave_addrs:
            _relay = _Relay(dev_addr=dev_addr, slave_addr=slave_addr)
            self._relays.append(_relay)
        # DISPLAY KEYS
        self._display_key = None
        self._display_keys = {'OPEN': self._relays[0], 'CLOSE': self._relays[1], 'FORWARD': self._relays[2],
                              'STOP FORWARD': self._relays[2], 'BACK': self._relays[2], 'LAST': self._relays[2],
                              'NEXT': self._relays[3]}
        # THREAD
        self._thread = None
        self._thread_switch = False
        self._thread_ts = 0

    def _working(self):
        while self._thread_switch:
            print(1)
            if self._display_key is not None:
                self._display_keys[self._display_key].open()
                print(self._display_key, True)
                self.sign_display_show.emit(self._display_key)
                print(self._thread_ts)
                time.sleep(self._thread_ts)
                self._display_keys[self._display_key].close()
                print(self._display_key, False)
                self._thread_switch = False
            print(2)
            self._thread_stop()

    def _thread_start(self):
        self._thread_switch = True
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _thread_stop(self):
        self._thread_switch = False

    def set_display_key(self, display_key):
        self._display_key = display_key
        if display_key in ['LAST', 'NEXT', 'BACK', 'STOP DORWARD']:
            self._thread_ts = 0.2
        #elif self._display_key == 'NEXT':
            #self._thread_ts = 0.2
        elif display_key in ['OPEN', 'CLOSE']:
            self._thread_ts = 0.5
        elif display_key == 'FORWARD':
            self._thread_ts = 0.6
        self._thread_start()

    def get_display_key(self):
        return self._display_key

    # TEST FUN
    def display_start(self):
        self.set_display_key(display_key='OPEN')

    def display_stop(self):
        self.set_display_key(display_key='CLOSE')

    def display_next(self):
        self.set_display_key(display_key='NEXT')

    def display_last(self):
        self.set_display_key(display_key='LAST')
