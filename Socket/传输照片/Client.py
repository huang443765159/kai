import socket
import time
import os
import sys
import struct


def sock_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('', 8888))
    except socket.error as msg:
        print(msg)
        print(sys.exit(1))

    while True:
        # filepath = input('input the file: ')
        # os.system("fswebcam -S 10 1.jpg")
        time.sleep(1)
        filepath = '/Users/huangkai/Desktop/ssh'
        fhead = struct.pack(b'128sl', bytes(os.path.basename(filepath).encode('utf-8')), os.stat(filepath).st_size)
        s.send(fhead)
        print('client filepath: {0}'.format(filepath))

        fp = open(filepath, 'rb')
        while 1:
            data = fp.read(1024)
            if not data:
                print('{0} file send over...'.format(filepath))
                break
            s.send(data)
        s.close()
        break


if __name__ == '__main__':
    sock_client()