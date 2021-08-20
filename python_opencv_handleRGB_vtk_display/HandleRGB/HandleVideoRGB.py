import cv2
import time
import threading
from PIL import Image


class HandleVideo(object):

    def __init__(self, rbg_callback, video_path):
        self._video_path = video_path + '/HandleRGB'
        print(self._video_path)
        self._rgb_callback = rbg_callback
        # THREAD
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        cap = cv2.VideoCapture(self._video_path + '/1.mp4')
        count = 0
        while 1:
            ret_val, frame = cap.read()
            print(ret_val)
            if ret_val:
                img = cv2.resize(frame, (64, 150))
                cv2.imwrite(self._video_path + f'/{count}.png', img)
                self._handle_rgb(img_path=self._video_path + f'/{count}.png')
                count += 1
            else:
                break
            time.sleep(0.01)
        cv2.destroyAllWindows()

    def _handle_rgb(self, img_path):
        img = Image.open(img_path)
        rgb_list = list(img.getdata())
        self._rgb_callback(rgb_list=rgb_list)


if __name__ == '__main__':

    def callback(rgb_list):
        pass

    test = HandleVideo(video_path='/Users/huangkai/Documents/PycharmProjects/LedControl/V4', rbg_callback=callback)
    while 1:
        time.sleep(1)
