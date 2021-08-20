import time
import serial
import threading


class MMW(object):

    def __init__(self):
        # SERIAL
        self.ser = serial.Serial(port='/dev/ttyAMA0', baudrate=115200, timeout=100)
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            self.ser.flushInput()  # 清理输入缓存
            self.ser.write(b'\xaa')
            # data = self.ser.read()
            # if data:
            #     print(data)
            time.sleep(0.1)


if __name__ == '__main__':

    mmw = MMW()
    while 1:
        time.sleep(1)
