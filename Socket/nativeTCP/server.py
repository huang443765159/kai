import socket
import time
'''
服务器关闭的是对方的客户端，也就是新连接的conn（client），所以不会报错
对方如果在循环里关闭客户端，那么就会报错
因为还要执行下一句

'''


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.settimeout(1)
server.bind(('192.168.50.165', 8888))
server.listen()
server.setblocking(False)

while 1:
    print('wait for connect', end=' ')
    try:
        conn, ip = server.accept()
        print(conn.getpeername()[0])
    except socket.error:
        print('nobody')
        time.sleep(1)
        continue
    while 1:
        try:
            data = conn.recv(10)
            if data == b'':
                print('空数据')
                conn.close()
                break
            else:
                print('RX', data)
        except socket.error:
            print("RT err")
            conn.close()
            break
        try:
            conn.send(b'xb1\xb2\xb3\xb4')
        except socket.error:
            print('TX err')
            conn.close()
            break
        time.sleep(2)
