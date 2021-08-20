import time
import struct
import serial
import threading
from typing import Dict


class Vl53l1x(object):

    def __init__(self):
        # SERIAL
        self.ser = serial.Serial(port='/dev/ttyAMA0', baudrate=115200)
        # SENSOR_DATA
        self._sensors_data = dict()  # type: Dict[int, int]
        self._data1_list = list()
        # PLT
        self._x = list()
        for i in range(1000):
            self._x.append(i)
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            msg = self.ser.read(18)
            if msg:
                print(msg)
                if msg[0: 2] == b'\xfe\x02':
                    for i in range(1, 9):
                        data = struct.unpack('!h', msg[2*i: 2*(i+1)])[0]
                        self._sensors_data[i] = data
                self._data1_list.append(self._sensors_data[1])
                print(f'裸片={self._sensors_data[1]}')
            time.sleep(0.1)


if __name__ == '__main__':

    test = Vl53l1x()

    while 1:
        time.sleep(1)
