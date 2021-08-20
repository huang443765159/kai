import time
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot


class SearchNum(QObject):
    sign_output = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        # 【1】THREAD 声明
        self._thread = QThread()  # 声明：声明一个实例
        self.moveToThread(self._thread)  # 声明2：把自己这个类移动到这个新线程里
        self._thread.started.connect(self.working)  # 多线程只能链接一个函数
        print('Main_Thread_ID={}'.format(int(QThread.currentThreadId())))

    # 【2】被并行的函数
    @pyqtSlot()
    def working(self):  # 只在这个函数块里面的有可能是在多线程
        num = 0
        while 1:
            num += 1
            print('Child_Thread_ID={}'.format(int(QThread.currentThreadId())), num)
            time.sleep(1)
            self.sign_output.emit(num)
            # print(threading.currentThread())

    def start(self):
        # 【3】并行启动
        self._thread.start()


if __name__ == '__main__':
    # 【4】QT运行环境
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    num1 = SearchNum()
    num2 = SearchNum()
    num1.start()
    num2.start()
    num1.sign_output.connect(print)
    num2.sign_output.connect(print)
    print('the child thread is {} '.format(QThread.currentThread()))

    sys.exit(app.exec_())

'''
多线程的最小系统 V20191117

特点：
1-使用QT方法
2-使用QT信号
3-线程的并行对象仅能是一个具体的函数，一个类不可以有多个函数进入到多个线程
4-While 1 配合 sleep使用，用来降低CPU占用率或控制运行频率
'''