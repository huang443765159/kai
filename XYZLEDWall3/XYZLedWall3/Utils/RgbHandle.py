import cv2
import time
import threading
from PIL import Image
from XYZLedWall3.Utils.CONST import CONST


class RgbHandle(object):

    def __init__(self, show_path, rgb_callback):
        self._show_path = show_path
        self._rgb_callback = rgb_callback
        # ATTR
        self._thread = dict()
        self._thread_switch = {1: False, 2: False}
        self._show = str()

    def _working(self, video_path, bot_id):
        cap = cv2.VideoCapture(video_path)
        img_id = 0
        while 1:
            if self._show != video_path:
                cv2.destroyAllWindows()
                cap = cv2.VideoCapture(self._show)
                video_path = self._show
            if self._thread_switch[bot_id]:
                ret_val, frame = cap.read()
                if ret_val:
                    img = cv2.resize(frame, (CONST.LED.COLS, CONST.LED.ROWS))
                    self._rgb_handle(img=img, img_id=img_id, bot_id=bot_id)
                    img_id += 1
                else:
                    self._thread_switch[bot_id] = False
                    break
                time.sleep(CONST.LED.DELAY)
        cv2.destroyAllWindows()

    def read_video(self, video_id: int, bot_id: int):
        self._show = self._show_path + '/Shows/' + CONST.SHOW.VIDEO[video_id]
        if self._thread_switch[bot_id] is False:
            video_path = self._show_path + '/Shows/' + CONST.SHOW.VIDEO[video_id]
            self._thread[bot_id] = threading.Thread(target=self._working, args=(video_path, bot_id, ))
            self._thread[bot_id].daemon = True
            self._thread_switch[bot_id] = True
            self._thread[bot_id].start()

    def read_img(self, img_id: int, bot_id: int):
        self._show = self._show_path + '/Shows/' + CONST.SHOW.IMG[img_id]
        img = cv2.imread(self._show)
        img = cv2.resize(img, (CONST.LED.COLS, CONST.LED.ROWS))
        self._rgb_handle(img=img, img_id=0, bot_id=bot_id)

    def _rgb_handle(self, img, img_id, bot_id):
        cv2.imwrite(self._show_path + f'/Shows/{img_id}_{bot_id}.png', img)
        new_img = Image.open(self._show_path + f'/Shows/{img_id}_{bot_id}.png')
        rgb_list = list(new_img.getdata())
        self._rgb_callback(rgb_list=rgb_list, bot_id=bot_id)

    def stop(self):
        for bot_id in self._thread_switch.keys():
            self._thread_switch[bot_id] = False
