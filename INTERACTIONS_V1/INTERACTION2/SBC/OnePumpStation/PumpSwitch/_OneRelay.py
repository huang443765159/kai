

class I2cRelay(object):

    def __init__(self, sys_judge, dev_addr, slave_addr):
        self._sys_judge = sys_judge
        if sys_judge is not None:
            import smbus
            self._dev_addr = dev_addr
            self._slave_addr = slave_addr
            # I2C BUS
            self._bus = smbus.SMBus(1)

    def open(self):
        if self._sys_judge is None:
            pass
        else:
            self._bus.write_byte_data(self._dev_addr, self._slave_addr, 0xff)

    def close(self):
        if self._sys_judge is None:
            pass
        else:
            self._bus.write_byte_data(self._dev_addr, self._slave_addr, 0x00)

    def get_relay_state(self):
        if self._sys_judge is not None:
            return True if self._bus.read_byte_data(self._dev_addr, self._slave_addr) else False
        else:
            pass


class GPIORelay(object):

    def __init__(self, sys_judge, pin):
        self._sys_judge = sys_judge
        if sys_judge is not None:
            import RPi.GPIO as GPIO
            self._gpio = GPIO
            self._pin = pin
            # GPIO
            self._gpio.setmode(GPIO.BCM)
            self._gpio.setwarnings(False)
            self._gpio.setup(self._pin, GPIO.OUT)

    def open(self):
        if self._sys_judge is not None:
            self._gpio.output(self._pin, 0)
        else:
            pass

    def close(self):
        if self._sys_judge is not None:
            self._gpio.output(self._pin, 1)
        else:
            pass

    def get_relay_state(self):
        if self._sys_judge is not None:
            return True if not self._gpio.read(self._pin) else False
        else:
            pass
