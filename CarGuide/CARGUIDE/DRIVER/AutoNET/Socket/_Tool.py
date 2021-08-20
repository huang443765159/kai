import socket


def get_my_ip():
    ip = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('100.100.100.100', 1000))
        ip = s.getsockname()[0]
        s.close()
    except socket.error as err:
        print('ERROR', 'GET_MY_IP', err)
    return ip
