import struct


def pack(msg_head):
    num_list = [7, 89, 69]
    # 表示包头
    msg = msg_head
    # 表示包的长度
    msg += struct.pack('H', len(num_list))
    for i in num_list:
        msg += struct.pack('H', int(i))
    return msg


def unpack(data):
    if data[0] == 0xbb:
        data_sum = struct.unpack('H', data[1:3])[0]
        print(data_sum)
        # 轮询把后边包的数据取出来
        stand = 0
        data_list = list()
        for i in range(data_sum):
            stand += 2
            sensor_data = struct.unpack('H', data[1+stand:3+stand])[0]
            print(sensor_data)
            data_list.append(sensor_data)
        print(data_list)


if __name__ == '__main__':
    data1 = pack(b'\xbb')  # 设置包头
    print(data1)
    unpack(data1)
