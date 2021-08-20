import threading
import pigpio
import time
import os

BAUD = 115200


class TOF(object):

    def __init__(self, rx_pin, tx_pin, data_cb):
        self._rx_pin = rx_pin
        self._tx_pin = tx_pin
        self._data_cb = data_cb
        # PI
        self._msg = bytes()
        self._pi = pigpio.pi()
        if not self._pi.connected:
            os.system('sudo pigpiod')
            time.sleep(1)
            self._pi = pigpio.pi()
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        self._pi.set_mode(self._rx_pin, pigpio.INPUT)
        self._pi.set_mode(self._tx_pin, pigpio.OUTPUT)
        pigpio.exceptions = False
        self._pi.bb_serial_read_close(self._rx_pin)
        pigpio.exceptions = True
        self._pi.bb_serial_read_open(self._rx_pin, BAUD, 8)
        while 1:
            count, data = self._pi.bb_serial_read(self._rx_pin)
            if count:
                self._msg += data
                if self._msg[0: 1] == b'd':
                    self._data_cb(msg=self._msg[3:-5])
                    self._msg = bytes()

    def send(self, msg):
        self._pi.wave_clear()
        self._pi.wave_add_serial(self._tx_pin, BAUD, msg)
        data = self._pi.wave_create()
        self._pi.wave_send_once(data)
        if self._pi.wave_tx_busy():
            pass
        self._pi.wave_delete(data)


if __name__ == '__main__':

    def data_cb(msg):
        print(f'距离物体{int(msg)}mm')

    tof = TOF(rx_pin=15, tx_pin=14, data_cb=data_cb)
    # tof.send(b'\x50\x06\x00\x38\x00\x02\x84G')  # 修改到i2c模式
    while 1:
        tof.send(b'\x50\x03\x00\x34\x00\x01')
        time.sleep(1)
