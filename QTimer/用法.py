from PyQt5.QtCore import QObject, QTimer
'''
备注：
方法一是可以使用self._timer.stop()函数把timer停止掉
方法二是没办法使用stop()函数的
'''


class Timer(QObject):

    def __init__(self):
        super().__init__()
        # 用法一
        self._timer = QTimer()
        self._timer.setSingleShot(True)  # 设置为单次，False就是循环
        # self._timer.setInterval(1000)
        self._timer.start(1000)
        self._timer.timeout.connect(self._timer_v1)

    def _timer_v1(self):
        print('123')

    def timer_v2(self):
        self._timer.singleShot(1000, lambda: print('123456'))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    test = Timer()
    sys.exit(app.exec())
