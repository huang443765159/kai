import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
TRIG = 16
ECHO = 18
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
while 1:
    GPIO.output(TRIG, False)
    time.sleep(1.5)
    print("Waiting for sensor to settle")
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)
    pulse_start = time.time()

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = (pulse_end-pulse_start)
    print("Pulse duration =%1f " % pulse_duration)
    distance = (pulse_duration*343/2 * 100)
    if 400 > distance > 0.5:
        print(f'距离车 {round(distance, 0)}cm')
    else:
        print("Out of Range")