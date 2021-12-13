'''
1: pip3 install python-periphery
2: cd /dev
3: ls 查看是否有spidev1.0的口
4: CLK为时钟，MOSI=发送， MISO=接收
5：鹏师傅74HC595串行通信，需要找一个IO口给一个上沿电平，先设置为低然后spi发消息，然后设置为高，再设置为低
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
CS引脚默认打开，就可以不使用额外引脚了
'''

from periphery import SPI

# Open spidev0.0 with mode 0 and max speed 1MHz
spi = SPI("/dev/spidev0.0", 0, 1000000)  # 树莓派有2个SPI   CM4有5个SPI

tx_msg = b'\x00\x01'
tx_return = spi.transfer(tx_msg)
rx_msg = spi.read()

spi.close()

