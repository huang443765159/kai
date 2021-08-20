import os
import sys
from platform import platform
if 'macOS' in platform():
    print('Mac have no wifi module')
elif 'debian' in platform():
    sys.path.append('/home/pi/Desktop/')
    from WIFIBIOS_LINUX._RaspWifi import RaspWifi as WIFI
elif 'generic' in platform():
    sys.path.append('Desktop/')
    from WIFIBIOS_LINUX._UbuntuWifi import UbuntuWifi as WIFI
interface_names = ['wlan0', 'wlp2s0', 'wlp3s0']


class WifiBios(object):

    def __init__(self):
        # INTERFACE_NAME
        if 'macOS' not in platform():
            self._interface_name = None
            net_list = os.listdir('/sys/class/net')  # 返回是一个net下所有名字的列表
            for name in interface_names:
                if name in net_list:
                    self._interface_name = name
            WIFI(interface_name=self._interface_name)


if __name__ == '__main__':
    import time
    test_wifi = WifiBios()
    while 1:
        time.sleep(1)
