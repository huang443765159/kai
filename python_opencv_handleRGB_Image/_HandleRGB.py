import cv2
import numpy as np
from PIL import Image


class HandleRGB(object):

    def __init__(self, rgb_callback, img_path):
        self._img_path = img_path
        self._rgb_callback = rgb_callback
        # IMAGE
        self._img = cv2.imread(self._img_path + '/1.jpeg')
        self._new_img = cv2.resize(self._img, (68, 91))
        self._rows, self._cols, rgb = self._new_img.shape
        print(self._rows, self._cols)  # 3648 2736
        cv2.imwrite(self._img_path + '/new_1.jpeg', self._new_img)
        img = Image.open(self._img_path + '/new_1.jpeg')
        rgb = img.getdata()
        self.rgb_mapping(rgb_list=list(rgb))

    def rgb_mapping(self, rgb_list):
        rgb_dict = dict()
        new_rgb_dict = dict()
        for idx, rgb in enumerate(rgb_list):
            rgb_dict[idx] = rgb
        points = [i for i in range(68 * 91)]
        new_points = np.array(points).reshape(68, 91)
        for idx, one_list in enumerate(new_points):
            if idx % 2 != 0:
                new_points[idx] = list(reversed(one_list))
        p_id = 0
        for one_list in list(new_points.T):
            for idx in one_list:
                new_rgb_dict[idx] = rgb_dict[p_id]
                p_id += 1
        self._rgb_callback(rgb_dict=new_rgb_dict)


if __name__ == '__main__':
    import os
    test = HandleRGB(rgb_callback=None, img_path=os.getcwd())
