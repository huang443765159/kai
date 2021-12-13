import spidev

spi = spidev.SpiDev()
spi.open(0, 0)  # spi0 = 0, 0 / spi1 = 0, 1    spi0：适用于所有RPI版本的P1接头    spi1：仅适用于40针的P1接头
response = spi.xfer2([0x40, 0x00])
print('Result is: ', response)
spi.close()


import spidev
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 5000
to_send = [0x01, 0x02, 0x03]
spi.xfer(to_send)
