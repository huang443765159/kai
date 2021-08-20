import struct


def pack(msg_head, data_dict):
    msg = msg_head + struct.pack('H', len(data_dict))
    for i in data_dict.values():
        msg += struct.pack('H', i)
    return msg


def unpack(msg):
    if msg[0] == 0xaa:
        data_len = struct.unpack('H', msg[1:3])[0]
        data_dict = dict()
        stand = 0
        for i in range(data_len):
            stand += 2
            data_dict[i] = struct.unpack('H', msg[1 + stand: 3 + stand])[0]
        print(data_dict)


if __name__ == '__main__':

    _msg = pack(b'\xaa', {0: 1, 1: 2, 2: 3})
    unpack(_msg)
