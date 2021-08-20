import threading
import pigpio
import time
import os

BAUD = 9600

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, 1)


class LidarLid:

    def __init__(self, rx_pin: int):
        self._rx_pin = rx_pin
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
        while 1:
            count, data = self._pi.bb_serial_read(self._rx_pin)
            if count:
                print(data)
            time.sleep(0.01)

    def send(self, msg):
        self._pi.set_mode(self._rx_pin, pigpio.OUTPUT)
        self._pi.wave_clear()
        self._pi.wave_add_serial(self._rx_pin, BAUD, msg)
        data = self._pi.wave_create()
        self._pi.wave_send_once(data)
        if self._pi.wave_tx_busy():
            pass
        self._pi.wave_delete(data)
        time.sleep(0.008)
        self._pi.set_mode(self._rx_pin, pigpio.INPUT)
        pigpio.exceptions = False
        self._pi.bb_serial_read_close(self._rx_pin)
        pigpio.exceptions = True
        self._pi.bb_serial_read_open(self._rx_pin, BAUD, 8)


if __name__ == '__main__':

    tof = LidarLid(rx_pin=21)
    # tof.send(msg=b'\x55\x55\x02\x03\x00\x02')  # CLOSE
    tof.send(msg=b'\x55\x55\x02\x03\x00\x01')  # OPEN
    while 1:
        time.sleep(1)
