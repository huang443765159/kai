import os
import time
import threading
wifi = {'M87OFFICE5G': '18610247958',
        'M87_RP_5G': '1234567890',
        '1927_JOBS': '18610247958',
        'M87_RP': '1234567890'}


class UbuntuWifi(object):

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
                wifi_name = self._scan()
                os.system(f'nmcli dev wifi connect {wifi_name} password {wifi[wifi_name]}')
            time.sleep(self._interval_frequency)

    def _scan(self):
        print('Scanning....')
        for wifi_name in wifi.keys():
            command = """iwlist {} scan | grep -ioE 'ssid:"(.*{}.*)'"""
            wifi_in_scan = os.popen(command.format(self._interface_name, wifi_name))
            wifi_in_scan = list(wifi_in_scan)
            if 'Device or resource busy' in wifi_in_scan:
                return None
            else:
                wifi_list = [item.lstrip('SSID:').strip('"\n') for item in wifi_in_scan]
                if wifi_list:
                    return wifi_name

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
    _test = UbuntuWifi('wlp3s0')
    while 1:
        time.sleep(1)
