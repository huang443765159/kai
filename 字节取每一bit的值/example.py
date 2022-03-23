b = 16


def get_bit_val(byte, index):
    if byte & (1 << index):
        return 1
    else:
        return 0


for i in range(8):
    a = get_bit_val(byte=b, index=i)
    print(i, a)
