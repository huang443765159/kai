'''
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
'''

import board
from time import sleep
import neopixel

pixels = neopixel.NeoPixel(board.D18, 8)

pixels.fill((0, 255, 0))

pixels[0] = (255, 0, 0)

while True:
    for x in range(0, 8):
        pixels[x] = (255, 0, 0)
        sleep(0.1)
        pixels.fill((0,255,0))

    for x in range(0, 8):
        pixels[x] = (255, 0, 0)
        sleep(0.1)
        pixels.fill((0,255,255))

    for x in range(0, 8):
        pixels[x] = (255, 0, 0)
        sleep(0.1)
        pixels.fill((0,0,255))

    for x in range(0, 8):
        pixels[x] = (0, 255, 0)
        sleep(0.1)
        pixels.fill((255,255,127))

    for x in range(0, 8):
        pixels[x] = (0, 255, 0)
        sleep(0.1)
        pixels.fill((255, 255, 0))
