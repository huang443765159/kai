# 左移动
a = 0xaabbcc
b = a << 8
print(hex(b))
# 右移动
c = a >> 8
print(hex(c))
# & 都为1则保留，否则为0, 取bb
d = c & 0x00ff
print(hex(d))
# | 其中一个不为0则保留非0位，都为1则保留大的位
e = c | 0x00ff
print(hex(e))

