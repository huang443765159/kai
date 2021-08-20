import socket
import platform


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


def get_socket_buffer_size():
    buffer_size = 4194304
    if platform.system() == 'Darwin':
        release = platform.release().split('.')
        mac_ver = 0
        for idx, num in enumerate(release):
            mac_ver += int(num) / 10 ** idx
        if mac_ver < 18:
            buffer_size = 2097152
    return buffer_size

