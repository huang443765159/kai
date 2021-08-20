# import smbus
'''
打开ℹ2c接口，然后终端 sudo i2cdetect -y i 查看address
就是地址

'''

# bus = smbus.SMBus(1)
# address = 0x29
# slave_addr = 0x10
# data = b'\x01'
#
# bus.write_byte_data(address, slave_addr, data)

# while 1:
#     # data = bus.read_byte_data(address, 0)
#     data = bus.read_i2c_block_data(address, slave_addr, 8)  # 最后一位是字节
#     # data = bus.read_data(address)
import time
import smbus
import threading


class I2c(object):
    def __init__(self, dev_address, register_addr):
        self._dev_addr = dev_address  # 设备地址
        self._reg_addr= register_addr # 要写入信息的寄存器地址
        self._bus = smbus.SMBus(1)
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            data = self._bus.read_byte_data(self._dev_addr, self._reg_addr)  # 读取1字节数据
            # data = self._bus.read_i2c_block_data(self._dev_addr, self._reg_addr, int)  # 最多可读取32位字节数据，返回是一个列表
            print(data)
            time.sleep(1)

    def write_data(self, data):
        self._bus.write_byte_data(self._dev_addr, self._reg_addr, data)  # 写入1字节数据
        # self._bus.write_i2c_block_data(self._dev_addr, self._reg_addr, [data]) # 写入最         多32位字节的数据


if __name__ == '__main__':
    i2c = I2c(0x10, 0x01)
    i2c.write_data(0xff)
    while 1:
        time.sleep(1)
