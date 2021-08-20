import time
import random
from rpi_ws281x import Adafruit_NeoPixel, Color


LED_COUNT = 30
LED_PIN = 18
LED_BRIGHTNESS = 10
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_INVERT = False

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

strip.begin()

for i in range(0, strip.numPixels()):
    strip.setPixelColor(i, Color(0, 0, 255))
strip.show()
