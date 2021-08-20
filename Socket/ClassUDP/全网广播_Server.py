# udp_gb_server.py
'''服务端（UDP协议局域网广播）'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 1060

network = '<broadcast>'
while 1:
    s.sendto('Client broadcast message!'.encode('utf-8'), (network, PORT))