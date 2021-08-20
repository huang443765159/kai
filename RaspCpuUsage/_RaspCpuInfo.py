import time
import threading
from PyQt5.QtCore import QObject, pyqtSignal


class CpuInfo(QObject):

    sign_cpu_info = pyqtSignal(float, dict)  # temp, usage

    def __init__(self, data_cb):
        super().__init__()
        self._data_cb = data_cb
        # CPU USAGE
        self._cpu_usage = dict()
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            # TEMP
            file = open('/sys/class/thermal/thermal_zone0/temp')
            temp = float(file.read()) / 1000
            file.close()
            # USAGE
            cpu_usage_start = self._get_cpu_usage()
            time.sleep(1)
            cpu_usage_end = self._get_cpu_usage()
            for cpu_id in cpu_usage_start.keys():
                idle_data_start = cpu_usage_start[cpu_id][0]
                idle_data_end = cpu_usage_end[cpu_id][0]
                idle_time_start = cpu_usage_start[cpu_id][1]
                idle_time_end = cpu_usage_end[cpu_id][1]
                cpu_usage = (1 - (idle_data_end - idle_data_start) / (idle_time_end - idle_time_start)) * 100
                self._cpu_usage[cpu_id] = round(cpu_usage, 2)
            self._data_cb(cpu_temp=temp, cpu_usage=self._cpu_usage)
            self.sign_cpu_info.emit(temp, self._cpu_usage)

    @staticmethod
    def _get_cpu_usage():
        cpu_usage_info = dict()
        file = open('/proc/stat', 'r')
        cpu_lines = [line.split(' ') for content in file.readlines() for line in content.split('\n') if
                     line.startswith('cpu')]
        for cpu_line in cpu_lines:
            if '' in cpu_line:
                cpu_line.remove('')
            print(cpu_line)
            cpu_data = [cpu_line[0]] + list(float(i) for i in cpu_line[1:])
            cpu_usage_info[cpu_data[0]] = [cpu_data[4], sum(cpu_data[1: 11])]
        return cpu_usage_info


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    def _data_cb(cpu_temp, cpu_usage):
        print(f'TEMP={cpu_temp}℃\nUSAGE={cpu_usage}')

    usage = CpuInfo(data_cb=_data_cb)
    usage.sign_cpu_info.connect(print)

    sys.exit(app.exec_())
