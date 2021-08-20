# print(int('00000001', 2))  1
# print(int('00000011', 2))  3
# print(int('00000111', 2))  7
# print(int('00001111', 2))  15
# print(int('00000000', 2))
# print(int('11111111', 2))
# b00000001 1
# b00000010 2
# b00000100 4
# b00001000 8

# a = 7
# a |= (0x01 << 3)
# print(a)
#
#
# print(a & 0x00ff)

import smbus


class I2c(object):

    def __init__(self, dev_addr=0x26, reg_addr=0x11):
        self._dev_addr = dev_addr
        self._reg_addr = reg_addr
        self._bus = smbus.SMBus(0)

    def choose_channel(self, channel_id: int):
        self._bus.write_byte(0x70, 1 << channel_id)

    def read_byte_data(self):
        self._bus.write_byte(self._dev_addr, self._reg_addr)
        data = self._bus.read_byte(self._dev_addr)
        return data & 0x00ff

    def write_byte_data(self, data: int):
        self._bus.write_byte_data(self._dev_addr, self._reg_addr, data)

    def write_num_data(self, num: int, state: bool):
        state_from_device = self.read_byte_data()
        if state:
            state_from_device |= (0x01 << num)
        else:
            state_from_device &= ~(0x01 << num)
        self.write_byte_data(state_from_device)


if __name__ == '__main__':
    import time
    test = I2c()
    test.choose_channel(0)
    for i in range(0, 4):
        test.write_num_data(i, True)
    test.choose_channel(1)
    for i in range(0, 2):
        test.write_num_data(i, True)
    time.sleep(1)
    # test.choose_channel(0)
    # for i in range(0, 4):
    #     test.write_num_data(i, False)
    # time.sleep(1)
    # test.choose_channel(1)
    # for i in range(0, 2):
    #     test.write_num_data(i, False)
