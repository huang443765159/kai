import os
import time
import pigpio
import threading

BAUD = 9600


class Liquid(object):

    def __init__(self, rx_pin, tx_pin, data_cb):
        self._rx_pin = rx_pin
        self._tx_pin = tx_pin
        self._data_cb = data_cb
        # PIGPIO
        self._pi = pigpio.pi()
        if not self._pi.connected:
            os.system('sudo pigpiod')
            self._pi = pigpio.pi()
        self._pi.set_mode(self._rx_pin, pigpio.INPUT)
        self._pi.set_mode(self._tx_pin, pigpio.OUTPUT)
        pigpio.exceptions = False
        self._pi.bb_serial_read_close(self._rx_pin)
        pigpio.exceptions = True
        self._pi.bb_serial_read_open(self._rx_pin, BAUD, 8)
        # ATTR
        self._thread_ts = 1
        self._msg = bytes()
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            count, data = self._pi.bb_serial_read(self._rx_pin)
            if count:
                self._msg += data
                if len(self._msg) == 4:
                    if (self._msg[0] + self._msg[1] + self._msg[2]) & 0x00ff == self._msg[3]:
                        self._data_cb(module='LIQUID', data=self._msg[1] * 256 + self._msg[2])
                        self._msg = bytes()
            time.sleep(self._thread_ts)

    def write_date(self, msg):
        self._pi.wave_clear()
        self._pi.wave_add_serial(self._tx_pin, BAUD, msg)
        data = self._pi.wave_create()
        self._pi.wave_send_once(data)
        if self._pi.wave_tx_busy():
            pass
        self._pi.wave_delete(data)

    def set_thread_ts(self, thread_ts):
        self._thread_ts = thread_ts

    def get_thread_ts(self):
        return self._thread_ts


if __name__ == '__main__':

    def _data_cb(module, data):
        print(module, data)

    liquid = Liquid(rx_pin=15, tx_pin=14, data_cb=_data_cb)
