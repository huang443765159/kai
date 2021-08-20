import os
import time
import threading
# 树莓派需要先把账号密码存入conf文件中  /etc/wpa_supplicant/wpa_supplicant.conf


class RaspWifi(object):

    def __init__(self, interface_name, interval_frequency=1):
        self._interface_name = interface_name
        # THREAD
        self._interval_frequency = interval_frequency
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            if not self._is_wifi_connected():
                print('Connecting....')
                wifi_id = self._get_target_wifi_id()
                os.system(f'wpa_cli -i wlan0 select_network {wifi_id}')
            time.sleep(self._interval_frequency)

    def _get_target_wifi_id(self):
        # 把conf文件中存储的wifi和wifi_id拿出来
        wifi_in_conf = os.popen('wpa_cli -i wlan0 list_network')
        lines = [x for x in wifi_in_conf.read().split('\n') if x != '']
        wifi = dict()
        for line in lines[1:]:
            one_wifi_info = line.split('\t')
            wifi[one_wifi_info[1]] = one_wifi_info[0]
        for key in wifi.keys():
            #  扫描wifi并把和conf文件中一直的wifi名字提取出来
            print('Scanning....')
            command = """iwlist {} scan | grep -ioE 'ssid:"(.*{}.*)'"""
            wifi_in_scan = os.popen(command.format(self._interface_name, key))
            wifi_in_scan = list(wifi_in_scan)
            if 'Device or resource busy' in wifi_in_scan:
                return None
            else:
                wifi_list = [item.lstrip('SSID:').strip('"\n') for item in wifi_in_scan]
                if wifi_list:
                    return wifi[key]

    def _is_wifi_connected(self):
        result = os.popen('iw {} link'.format(self._interface_name))
        if 'Connected to ' in result.read():
            print('success')
            wifi_connected = True
        else:
            print('failed')
            wifi_connected = False
        return wifi_connected


if __name__ == '__main__':
    _test = RaspWifi('wlan0')
