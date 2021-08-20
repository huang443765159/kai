import socket
import time


while 1:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        client.settimeout(1)
        client.connect(('192.168.50.165', 8888))
        client.setblocking(False)
        print('success')
    except socket.error:
        print('wait for connect')
        time.sleep(1)
        continue
    while 1:
        try:
            data = client.recv(10)
            if data == b'':
                print('kong')
                break
            else:
                print(data)
        except socket.error:
            pass
        try:
            client.send(b'\xe0\xe1\xe2')
        except socket.error:
            print('TX err')
            client.close()
            break
        time.sleep(2)
