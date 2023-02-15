# from pyqtgraph1 import examples
# examples.run()

import time
import random
import threading
import pyqtgraph as pg


class AddCurve(object):

    def __init__(self):
        # PYQT_GRAPH  添加一个widget
        self._widget = pg.GraphicsLayoutWidget(show=True)
        self._widget.setWindowTitle('VL53L1对比')
        self._plt = self._widget.addPlot()
        self._plt.addLegend()  # 添加图例
        self._plt.addLine(y=300, pen='y')  # 添加y轴总高，并设置为黄色
        # CURVE 折线
        self._data1 = list()
        self._curve1 = self._plt.plot(self._data1, pen=pg.mkPen('b', width=3), name='blue curve')
        self._data2 = list()
        self._curve2 = self._plt.plot(self._data2, pen=pg.mkPen('r', width=3), name='red curve')
        # TIMER
        self._timer = pg.QtCore.QTimer()
        self._timer.timeout.connect(self._update)
        self._timer.start(1000 / 29970)
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _update(self):
        if self._data1:
            self._data1[: -1] = self._data1[1:]  # 向左移动
            self._curve1.setData(self._data1)
        if self._data2:
            self._data2[: -1] = self._data2[1:]
            self._curve2.setData(self._data2)
        time.sleep(1 / 500)

    def _working(self):  # 实时添加点
        while 1:
            self._data1.append(random.randint(0, 100))
            self._data2.append(random.randint(30, 500))
            time.sleep(1 / 500)


if __name__ == '__main__':
    test = AddCurve()
    pg.mkQApp().exec_()  # 执行函数
