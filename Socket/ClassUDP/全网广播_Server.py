# udp_gb_server.py
'''服务端（UDP协议局域网广播）'''

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 54188

# s.bind(('', 54188))  # 绑定后自己了一监听此端口
network = '<broadcast>'
while 1:
    s.sendto(b'\xaa', (network, 3333))
    time.sleep(0.1)
