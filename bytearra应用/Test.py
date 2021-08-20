# bytearray

msg_len = 2
msg = bytearray(msg_len)

msg.append(2)  # append 添加int
msg.extend(b'\xaa')  # extern 添加bytes
msg.extend(bytearray('Hello', 'utf8'))

print(msg)


msg2 = bytes(msg_len)
# 无 append 和 extern功能
print(msg2)
