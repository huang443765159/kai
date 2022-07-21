import cv2
import time
import threading
from typing import Callable
from multiprocessing import Pipe, Process, get_context

import numpy as np

mp = get_context('spawn')


class OneProcess:

    def __init__(self):
        self._pipe_main, pipe_sub = Pipe()
        thread = threading.Thread(target=self._pip_main_recv, daemon=True)
        thread.start()
        self._process = Process(target=self._process_working, args=(pipe_sub, ), daemon=True)
        self._process.start()

    def _pip_main_recv(self):
        while 1:
            bytes_array = self._pipe_main.recv()
            frame = cv2.imdecode(bytes_array, 1)
            print(frame)

    def _process_working(self, pipe_sub):
        cap = cv2.VideoCapture(0)
        while 1:
            ret, frame = cap.read()
            if ret:
                _, send_data = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
                if _:
                    pipe_sub.send(send_data)


if __name__ == '__main__':

    test = OneProcess()
    while 1:
        time.sleep(1)

