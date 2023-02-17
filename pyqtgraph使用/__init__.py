from PyQt5.QtWidgets import *
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

plt = pg.plot()
plt.setWindowTitle('pyqtgraph example: Legend')
plt.addLegend()

c1 = plt.plot([1, 3, 2, 4], pen='r', name='red plot')
c2 = plt.plot([2, 1, 4, 3], pen='g', fillLevel=0, fillBrush=(255, 255, 255, 30), name='green plot')
c3 = plt.addLine(y=4, pen='y')
# TODO: add legend item indicating "maximum value"

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QApplication.instance().exec_()
