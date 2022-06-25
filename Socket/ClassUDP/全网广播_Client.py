# udp_gb_client.py
'''客户端（UDP协议局域网广播）'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 1060

s.bind(('', 1060))
print('Listening for broadcast at ', s.getsockname())

while True:
    s.sendto(b'\xaa', ('192.168.50.111', 5000))  # 单点发送
    # data, address = s.recvfrom(65535)
    # print('Server received from {}:{}'.format(address, data.decode('utf-8')))  # 广播发送
