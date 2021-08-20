# udp_gb_server.py
'''客户端（UDP协议局域网广播）'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 1060

s.bind(('', PORT))
print('Listening for broadcast at ', s.getsockname())

while True:
    data, address = s.recvfrom(65535)
    print('Server received from {}:{}'.format(address, data.decode('utf-8')))