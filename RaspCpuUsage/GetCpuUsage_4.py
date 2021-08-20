import time
import psutil
import threading
from platform import system
from PyQt5.QtCore import QObject, pyqtSignal


class CpuInfo(QObject):

    sign_cpu_info = pyqtSignal(str, float, float, list)  # module, temp, total_usage ,kernel_usages

    def __init__(self,):
        super().__init__()
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread_interval = 1
        self._thread_switch = True
        self._thread.start()

    def _working(self):
        last_idle = last_total = 0
        while self._thread_switch:
            if system() == 'Darwin':
                self.sign_cpu_info.emit('MAC', 0.0, 0.0, psutil.cpu_percent(1, True))
            else:
                # RASP CPU
                usage_file = open('/proc/stat')
                cpu_data = [float(column) for column in usage_file.readline().strip().split()[1:]]
                idle_time, total_time = cpu_data[3], sum(cpu_data)
                idle_poor, total_poor = idle_time - last_idle, total_time - last_total
                last_idle, last_total = idle_time, total_time
                cpu_usage = round(100 * (1 - idle_poor / total_poor), 1)
                # RASP TEMP
                temp_file = open('/sys/class/thermal/thermal_zone0/temp')
                temp = float(temp_file.read()) / 1000
                self.sign_cpu_info.emit('RASP', round(temp, 0), cpu_usage, psutil.cpu_percent(1, True))
            time.sleep(self._thread_interval)

    def set_thread_interval(self, interval):
        self._thread_interval = interval

    def exit(self):
        self._thread_switch = False


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    _info = CpuInfo()
    _info.sign_cpu_info.connect(lambda a, b, c, d: print(f'MODULE={a}, TEMP={b}℃, TOTAL_USAGE={c}%, KERNEL_USAGE={d}'))

    sys.exit(app.exec_())