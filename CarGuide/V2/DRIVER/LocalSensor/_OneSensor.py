import threading
import time
import random
import signal
import sys

lock = threading.Lock()


class OneSensor(object):

    def __init__(self, sid, pin, data_cb):
        self._sid = sid
        self._pin = pin
        self._data_cb = data_cb

        self._thread = None
        self._thread_switch = False

        self._signal = signal
        self._signal.signal(signal.SIGINT, self.sys_quit)

    def _working(self):
        while self._thread_switch:
            lock.acquire()
            self._data_cb(sid=self._sid, data=random.randint(0, 100))
            lock.release()
            time.sleep(1/8)

    def launch(self):
        if self._thread_switch is False:
            self._thread = threading.Thread(target=self._working)
            self._thread.daemon = True
            self._thread_switch = True
            self._thread.start()

    def stop(self):
        if self._thread_switch:
            self._thread_switch = False
            self._thread.join()

    def sys_quit(self, signal_num, handle):
        print('sys quit')
        sys.exit(0)


if __name__ == '__main__':

    sensors = dict()
    sensors_data = dict()
    pin_list = [1, 2, 3]


    def _data_cb(sid, data):
        sensors_data[sid] = data
        if None not in sensors_data.values():
            print(sensors_data)
            for sid in sensors_data:
                sensors_data[sid] = None

    for _sid, _pin in enumerate(pin_list):
        sensors[_sid] = OneSensor(_sid, _pin, _data_cb)
        sensors_data[_sid] = None

    for sensor in sensors.values():
        sensor.launch()

    while 1:
        time.sleep(1)







