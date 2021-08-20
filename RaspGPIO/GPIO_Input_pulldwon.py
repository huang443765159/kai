import time
import threading
import RPi.GPIO as GPIO


class Test(object):

    def __init__(self, pin):
        self._pin = pin
        # GPIO
        GPIO.setmode(GPIO.BOARD)  # BCM=GPIO PIN  BOARD=RASP PIN
        GPIO.setwarnings(False)
        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # PUD_DOWN=下拉电阻  PUD_UP=上拉电阻
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            print(GPIO.input(self._pin))
            time.sleep(0.1)


if __name__ == '__main__':

    test = Test(22)
    while 1:
        time.sleep(1)
# 12 14 24 13, 15