from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
import configparser
import time
import os
try:
    import psutil
except:
    pass


class SysInfo(QObject):

    sign_state = pyqtSignal(float, float, int)  # cpu_temp, cpu_usage, mem_rss, mem_data

    def __init__(self, sps_monitor=1):
        super().__init__()
        self._sps = sps_monitor  # 时间间隔
        self._os_type = self.get_os_type()  # 获取电脑型号
        self._dir_root = self.get_root_path()  # 获取路径
        self._dev_type = 'Unknown'
        self._dev_id = 99
        if self._os_type == 'Mac':
            self._process = psutil.Process(os.getpid())  # 读取内存信息
            self._thread = QThread()
            self.moveToThread(self._thread)
            self._thread.started.connect(self._running)
            self._thread.start()

    @pyqtSlot()
    def _running(self):
        while 1:
            cpu_usage = self.get_cpu_usage()  # 获取内存比例
            cpu_temp = self.get_cpu_temp()  # 获取cpu温度
            mem_rss = self.get_memory_info()  # 获取设备类型，设备地址
            self.sign_state.emit(cpu_temp, cpu_usage, mem_rss)
            time.sleep(self._sps)

    @staticmethod
    def get_os_type():
        info = os.uname()
        os_type = 'Unknown'
        if info[0] == 'Darwin' and info[4] == 'x86_64':
            os_type = 'Mac'
        elif info[0] == 'Linux' and info[4] == 'armv7l':
            os_type = 'RaspberryPi'
        return os_type

    @staticmethod
    def get_root_path():
        root = os.path.dirname(os.path.abspath(__file__))
        for i in range(4):
            if root.endswith('CLIENT'):
                break
            root = os.path.dirname(root)
        dir_root = root + '/'
        return dir_root

    @staticmethod
    def get_cpu_temp():
        # cpu_temp = psutil.sensors_temperatures()['cpu-thermal'][0].current
        return 0

    def get_cpu_usage(self):
        return self._process.cpu_percent()

    def get_memory_info(self):
        mem_info = self._process.memory_info()
        mem_rss = mem_info.rss / 1024 / 1024
        # mem_data = mem_info.data / 1024 / 1024
        return mem_rss

    def get_device_info(self):
        path_1 = self._dir_root + '../Device.配置文件读写'
        path_2 = self._dir_root + 'CONFIG/Device.配置文件读写'
        if os.path.exists(path_1):
            ini_path = path_1
        else:
            ini_path = path_2
        device_ini = configparser.ConfigParser()
        device_ini.read(ini_path)
        self._dev_type = device_ini.get('Device', 'Type')
        self._dev_id = device_ini.getint('Device', 'ID')
        return self._dev_type, self._dev_id


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)

    sys_info = SysInfo()
    sys_info.sign_state.connect(print)

    sys.exit(app.exec_())
