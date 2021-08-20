import threading
import VL53L1X
import time


class Vl53l1x(object):

    def __init__(self, i2c_address):
        self._i2c_addr = i2c_address
        # TOF
        self._tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=self._i2c_addr)
        # self._roi = VL53L1X.VL53L1xUserRoi(6, 3, 9, 0)
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()
        self._x = 0
        self._y = 0

    def _working(self):
        self._tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=self._i2c_addr)
        self._tof.open()
        self._tof.start_ranging(1)
        while 1:
            dis = self._tof.get_distance()
            print(f'<DIS> {dis}')
            self._x += 1
            self._y += 1
            if self._x < 5 and self._y < 5:
                roi = VL53L1X.VL53L1xUserRoi(3 * self._x, (15 - 3 * self._y), (3 * self._x + 3), (15 - 3 * self._y - 3))
                self.set_roi(roi)
                print(f'[LEFT X]{roi.top_left_x}\r\n[LEFT Y]{roi.top_left_y}\r\n[RIGHT X]{roi.bot_right_x}\r\n[RIGHT Y]{roi.bot_right_y}')
            time.sleep(0.1)

    def stop(self):
        self._tof.stop_ranging()

    def set_period(self, period):
        self._tof.set_inter_measurement_period(period)

    def set_roi(self, roi):
        self._tof.set_user_roi(roi)


if __name__ == '__main__':

    vl = Vl53l1x(0x29)
    while 1:
        time.sleep(1)

'''
start_ranging(1) # 0 不变
                # 1 短距离模式
                # 2 中距离模式
                # 3 长距离模式
https://github.com/pimoroni/vl53l1x-python
'''