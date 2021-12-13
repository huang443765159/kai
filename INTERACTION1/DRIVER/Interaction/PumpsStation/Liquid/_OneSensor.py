import time
import random
import pigpio
import threading

BAUD = 9600


class OneSensor(object):

    def __init__(self, pi, sid, rx_pin, tx_pin, data_cb):
        self._pi = pi
        self._sid = sid
        self._rx_pin = rx_pin
        self._tx_pin = tx_pin
        self._data_cb = data_cb
        # PI
        self._pi.set_mode(self._rx_pin, pigpio.INPUT)
        self._pi.set_mode(self._tx_pin, pigpio.OUTPUT)
        pigpio.exceptions = False
        self._pi.bb_serial_read_close(self._rx_pin)
        pigpio.exceptions = True
        self._pi.bb_serial_read_open(self._rx_pin, BAUD, 8)
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
                        self._data_cb(sid=self._sid, data=self._msg[1] * 256 + self._msg[2])
                self._msg = bytes()
            time.sleep(1)


if __name__ == '__main__':
    import os


    def _data_cb(sid, data):
        print(sid, data)


    _pi = pigpio.pi()
    if not _pi.connected:
        os.system('sudo pigpiod')
        _pi = pigpio.pi()

    sensor = OneSensor(pi=_pi, sid=1, rx_pin=15, tx_pin=14, data_cb=_data_cb)
    # rx_pin=15, 24, 8, 12, 20
    # tx_pin=14, 23, 25, 7, 16
