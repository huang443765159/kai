import threading
import serial
import struct
import time

BAUD = 115200
SET_I2C_MODE = b'\x50\x06\x00\x38\x00\x02'
GET_DIS = b'\x50\x03\x00\x34\x00\x01\xc8\x45'


def get_crc_data(msg):
    crc_init = 0xffff
    for data in msg:
        data = data & 0x00ff
        crc_init ^= data
        for i in range(0, 8):
            if crc_init & 0x0001:
                crc_init >>= 1
                crc_init ^= 0xa001
            else:
                crc_init >>= 1
    crc_high, crc_low = crc_init & 0xff, crc_init >> 8
    print(crc_high, crc_low)
    print(struct.pack('B', crc_high) + struct.pack('B', crc_low))
    print(hex(crc_high), hex(crc_low))
    return struct.pack('B', crc_high), struct.pack('B', crc_low)


class WtVL53L1X(object):

    def __init__(self):
        # SERIAL
        self._ser = serial.Serial(port='/dev/ttyS0', baudrate=115200)
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            print(111)
            msg = self._ser.readline()
            print('msg', msg)
            if msg:
                print(msg)
            time.sleep(0.1)

    def set_i2c(self):
        crc_high, crc_low = get_crc_data(msg=SET_I2C_MODE)
        self._ser.write(SET_I2C_MODE + crc_high + crc_low)

    def get_dis(self):
        self._ser.write(GET_DIS)


if __name__ == '__main__':
    test = WtVL53L1X()
    while 1:
        time.sleep(1)
