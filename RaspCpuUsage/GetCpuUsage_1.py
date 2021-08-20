import time
import threading


class GetCpuUsage(object):

    def __init__(self, data_cb):
        self._data_cb = data_cb
        self._cpu_usage = dict()
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            cpu_start_infos = self._get_cpu_infos()
            time.sleep(1)
            cpu_end_infos = self._get_cpu_infos()
            for cpu_id in cpu_start_infos.keys():
                idle_start = cpu_start_infos[cpu_id][0]
                idle_end = cpu_end_infos[cpu_id][0]
                cpu_time_start = cpu_start_infos[cpu_id][1]
                cpu_time_end = cpu_end_infos[cpu_id][1]
                cpu_usage = (1 - (idle_end - idle_start) / (cpu_time_end - cpu_time_start)) * 100
                self._cpu_usage[cpu_id] = cpu_usage
            # print(self._cpu_usage)
            self._data_cb(module=self._cpu_usage)

    @staticmethod
    def _get_cpu_infos():
        cpu_infos = dict()
        with open('/proc/stat', 'r') as f:
            cpu_lines = [line.split(' ') for content in f.readlines() for line in content.split('\n') if
                         line.startswith('cpu')]
            for cpu_line in cpu_lines:
                if '' in cpu_line:
                    cpu_line.remove('')
                cpu_line = [cpu_line[0]] + list(float(i) for i in cpu_line[1:])
                cpu_id = cpu_line[0]
                idle = cpu_line[4]
                cpu_time = sum(cpu_line[1: 11])
                cpu_infos[cpu_id] = [idle, cpu_time]
            return cpu_infos


if __name__ == '__main__':

    def _data_cb(module):
        print(module)

    _test = GetCpuUsage(_data_cb)
    while 1:
        time.sleep(1)
