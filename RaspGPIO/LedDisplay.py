"""
GPIO 在未设置之前是0v电压
GPIO.output(1) 或者HIGH之后是3.3v高电压
GPIO.output(0) 或者LOW之后是0V低电压
GPIO.cleanup() 有1V残留电压
"""


import time
import RPi.GPIO as GPIO


class LedDisplay(object):

    def __init__(self, pins, data_cb):
        self._pins = pins
        self._data_cb = data_cb
        # GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        for pin in self._pins:
            GPIO.setup(pin, GPIO.OUT)
        # SHOW
        self._show = {'WELCOME': None, 'FORWARD': [1, 1, 1, 1, 0], 'STOP': [1, 1, 1, 0, 1], 'BACK': [1, 1, 0, 1, 1],
                      'WASH START': [1, 0, 1, 1, 1], 'WASH END': [0, 1, 1, 1, 1]}

    def set_display(self, show):
        if show in self._show.keys():
            if show == 'WELCOME':
                GPIO.cleanup()
            else:
                for idx, state in enumerate(self._show[show]):
                    GPIO.output(self._pins[idx], state)
            self._data_cb(module=show, code='DISPLAY', value=True)


if __name__ == '__main__':

    _pins = [35, 36, 37, 38, 40]
    led = LedDisplay(pins=_pins, data_cb=1)
    led.set_display('FORWARD')
    time.sleep(2)
    led.set_display('STOP')
    time.sleep(2)
    led.set_display('BACK')
    time.sleep(2)
    led.set_display('WASH START')
    time.sleep(2)
    led.set_display('WASH END')
    time.sleep(2)
    led.set_display('WELCOME')

