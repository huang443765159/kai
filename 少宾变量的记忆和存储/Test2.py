import time
from Test.test1 import OneSensor


class SensorLocal(object):

    def __init__(self, pin_list):
        self._pin_list = pin_list

        self._sensors = dict()
        self._sensors_data = dict()
        self._sensors_memory_data = dict()

        for sid, pin in enumerate(self._pin_list):
            self._sensors[sid] = OneSensor(sid=sid, pin=pin, data_cb=self._data_cb)
            self._sensors_data[sid] = None
            self._sensors_memory_data[sid] = None

    def _data_cb(self, sid, data):
        self._sensors_data[sid] = data
        if None not in self._sensors_data.values():
            # print(self._sensors_data)
            for sid in self._sensors_data:
                self._sensors_data[sid] = None
        if self._sensors_memory_data[sid] != self._sensors_data[sid]:
            self._sensors_memory_data[sid] = self._sensors_data[sid]
            print(self._sensors_data)

    def launch(self):
        for sensor in self._sensors.values():
            sensor.launch()

    def stop(self):
        for sensor in self._sensors.values():
            sensor.stop()


if __name__ == '__main__':

    one_sensor = SensorLocal([1, 2, 3])
    one_sensor.launch()
    while 1:
        time.sleep(1)
