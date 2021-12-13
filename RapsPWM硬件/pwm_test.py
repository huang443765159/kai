import os
import time
import platform
if 'Linux' in platform.platform():
    import pigpio

#  hardware_PWM(pin, 频率0-125000hz, 0-125Mhz 100=100hz， 占空比0-1M=1000000) 指令间要有至少25ms的延迟，否则树莓派有可能会坏掉  BOARD=18


class Test(object):

    def __init__(self, pin, freq):
        self._pin = pin
        self._freq = freq
        self._pi = pigpio.pi()
        if not self._pi.connected:
            os.system('sudo pigpiod')
            time.sleep(0.5)
            self._pi = pigpio.pi()
            self._pi.set_mode(self._pin, pigpio.OUTPUT)
            self._pi.hardware_PWM(self._pin, self._freq, 0)

    def set_ena(self, switch: bool):
        self._pi.hardware_PWM(self._pin, self._freq, 430000 if switch else 370000)

    def stop(self):
        self._pi.hardware_PWM(self._pin, self._freq, 0)


if __name__ == '__main__':
    test = Test(pin=18, freq=200)
    test.set_ena(switch=True)
    time.sleep(1)
    test.set_ena(switch=False)
    test.stop()
