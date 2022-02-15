import struct


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


if __name__ == '__main__':
    # get_crc_data(msg=[0x02, 0x06, 0x00, 0x06, 0x00, 0x01])  # A8 38
    # get_crc_data(msg=b'\x02\x06\x00\x06\x00\x01')
    get_crc_data(b'\x50\x06\x00\x38\x00\x02')

    """
    Test_data
    [0x02, 0x06, 0x00, 0x06, 0x00, 0x01, 0xa8, 0x38]
    [0x01, 0x03, 0x02, 0x00, 0xd2, 0x38, 0x19]
    [0x01, 0x03, 0x00, 0x00, 0x00, 0x02, 0xc4, 0x0b]
    [0x01, 0x03, 0x04, 0x00, 0xdc, 0x00, 0xdd, 0xfb, 0x09]
    """

