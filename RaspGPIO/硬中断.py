import RPi.GPIO as GPIO
import threading
import time


class Test:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setwarnings(False)

        # THREAD
        self._thread = threading.Thread(target=self._working, daemon=True)
        self._thread.start()

    def _working(self):
        while True:
            GPIO.wait_for_edge(21, GPIO.BOTH)  # GPIO.FALLING 下降   GPIO.RISING 上升
            print(f'state={GPIO.input(21)}')


class Test2:

    def __init__(self, pin: int):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setwarnings(False)

        GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=100)  # GPIO.RISING  GPIO.FALLING
        GPIO.add_event_callback(pin, self._my_callback_one)
        # GPIO.add_event_callback(pin, self._my_callback_two)

    def _my_callback_one(self, pin: int):
        print(GPIO.input(pin))

    def _my_callback_two(self, pin: int):
        print(GPIO.input(21))


if __name__ == '__main__':
    test = Test()
    while 1:
        time.sleep(1)
