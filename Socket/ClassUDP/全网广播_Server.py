# udp_gb_server.py
'''服务端（UDP协议局域网广播）'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 54188

s.bind(('', 54188))
network = '<broadcast>'
while 1:
    data, addr = s.recvfrom(255)
    print(data, addr)
    # s.sendto('Client broadcast message!'.encode('utf-8'), (network, PORT))
