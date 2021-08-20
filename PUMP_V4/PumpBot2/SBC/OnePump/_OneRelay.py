

class I2CRelay(object):

    def __init__(self, dev_address, slave_address):
        self._dev_address = dev_address
        self._slave_address = slave_address
        self._err = False
        try:
            import smbus
            # I2C BUS
            self._bus = smbus.SMBus(1)
        except ImportError as err:
            self._err = True
            # print(err)

    def set_ena(self, ena: bool):
        if not self._err:
            self._bus.write_byte_data(self._dev_address, self._slave_address, 0xff if ena else 0x00)


class GPIORelay(object):

    def __init__(self, pin):
        self._pin = pin
        self._err = False
        try:
            import RPi.GPIO as GPIO
            self._gpio = GPIO
            # GPIO
            self._gpio.setmode(GPIO.BCM)
            self._gpio.setwarnings(False)
            self._gpio.setup(self._pin, GPIO.OUT)
        except ImportError as err:
            self._err = True
            # print(err)

    def set_ena(self, ena: bool):
        if not self._err:
            self._gpio.output(self._pin, 0 if ena else 1)
