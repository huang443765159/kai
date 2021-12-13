import os
import time
import multiprocessing
from threading import Thread
"""
pipe生成会把之前的变量全部复制一遍，所以需要使用的变量要放在pipe之前提前声明
此变量在各自进程执行，彼此不会互相影响，如果需要统一，则需要发送到对端来进行更改
"""


class OneProcess:

    def __init__(self):
        self._test_variable = 100
        self._pipe_main, pipe_sub = multiprocessing.Pipe()
        thread = Thread(target=self._pipe_main_recv, daemon=True)
        thread.start()
        self._process = multiprocessing.Process(target=self._process_working, args=(pipe_sub, ), daemon=True)
        self._process.start()

    def pip_main_send(self, data: bytes):
        if self._process.is_alive():
            self._pipe_main.send(data)
            print(f'MAIN_PROCESS_ID={multiprocessing.current_process}, TEST_VARIABLE={self._test_variable}')
            self._test_variable = 300

    def _pipe_main_recv(self):
        while 1:
            bytes_array = self._pipe_main.recv()
            print(f'DATA_RECV_FROM_SUB={bytes_array}')

    def _process_working(self, pipe_sub):
        ppid = os.getppid()
        ts_check_ppid = 0.0
        while True:
            if not pipe_sub.poll(timeout=1):
                if time.time() - ts_check_ppid > 2:
                    ts_check_ppid = time.time()
                    if os.getppid() != ppid:
                        break
            else:
                bytes_array = pipe_sub.recv()
                print(f'DATA_RECV_FROM_MAIN={bytes_array} CURRENT_ID={multiprocessing.current_process}'
                      f'TEST_VARIABLE={self._test_variable}')
                self._test_variable = 200


if __name__ == '__main__':
    test = OneProcess()
    while 1:
        test.pip_main_send(data=b'\xaa\xbb')
        time.sleep(1)
