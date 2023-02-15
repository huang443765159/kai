import time
import struct
import threading
import pyqtgraph as pg


a = bytes()

for i in range(int(30000 / 2)):
    a += struct.pack('!h', i * 2)

ts_start = time.time()
for i in range(int(len(a) / 2)):
    pressure = struct.unpack('!h', a[i * 2: (i + 1) * 2])[0]
print(time.time() - ts_start)


class Test:

    def __init__(self):
        self._widget = pg.GraphicsLayoutWidget(show=True)
        self._widget.setWindowTitle('TEST')
        self._plt = self._widget.addPlot()
        self._plt.addLegend()
        self._plt.addLine(y=2000, pen='y')
        self._data = [0 for i in range(1000)]
        self._curve = self._plt.plot(self._data, pen=pg.mkPen('b', width=3), name='Blue Curve')
        # THREAD
        self._thread_add = threading.Thread(target=self._update, daemon=True)
        self._thread_add.start()
        # self._thread_add = threading.Thread(target=self._working1, daemon=True)
        # self._thread_add.start()

    def _update(self):
        while True:
            for i in range(1998):
                self._data[: -1] = self._data[1:]
                self._data[-1] = i
                self._curve.setData(self._data)
            time.sleep(1 / 500)


if __name__ == '__main__':
    test = Test()
    pg.mkQApp().exec_()