import time
import threading
import RPi.GPIO as GPIO


class Test:

    def __init__(self, pin: int):
        self._pin = pin
        GPIO.setmode(GPIO.BCM)  # BCM=GPIO PIN  BOARD=RASP PIN
        GPIO.setwarnings(False)
        GPIO.setup(self._pin, GPIO.OUT)

    def set_ena(self, ena: bool):
        GPIO.output(self._pin, 1 if ena else 0)


if __name__ == '__main__':
    test = Test(21)
    test.set_ena(ena=True)
