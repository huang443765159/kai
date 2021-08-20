import socket
import time

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ('127.0.0.1', 8888)

while 1:
    try:
        udp.bind(address)
    except socket.error:
        print('failed')
        time.sleep(1)
        continue
    while 1:
        udp.sendto(b'\xb1\xb2', address)
        time.sleep(1)
        data = udp.recv(10)
        if data:
            print(data)
        else:
            print('RX err')
