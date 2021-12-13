import smbus
import RPi.GPIO as GPIO


class I2cRelay(object):

    def __init__(self, dev_addr, slave_addr):
        self._dev_addr = dev_addr
        self._slave_addr = slave_addr
        # BUS
        self._bus = smbus.SMBus(1)

    def open(self):
        self._bus.write_byte_data(self._dev_addr, self._slave_addr, 0xff)

    def close(self):
        self._bus.write_byte_data(self._dev_addr, self._slave_addr, 0x00)


class GPIORelay(object):

    def __init__(self, pin):
        self._pin = pin
        # GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self._pin, GPIO.OUT)

    def open(self):
        GPIO.output(self._pin, 0)

    def close(self):
        GPIO.output(self._pin, 1)


if __name__ == '__main__':
    import time

    _i2c = I2cRelay(0x11, 1)  # slave=1, 2, 3, 4
    _i2c.open()
    time.sleep(1)
    _i2c.close()

    _gpio = GPIORelay(19)  # pin=19, 13, 6, 5, 11, 9, 10, 22, 27
    _gpio.open()
    time.sleep(1)
    _gpio.close()
