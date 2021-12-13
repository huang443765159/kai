import numpy as np
from XYZLedWall3.Utils.CONST import CONST


def rbg_mapping(rgb_list):
    rgb_dict = dict()
    new_rgb_dict = dict()
    for idx, rgb in enumerate(rgb_list):
        rgb_dict[idx] = rgb
    led = [i for i in range(CONST.LED.COLS * CONST.LED.ROWS)]
    led_array = np.array(led).reshape(CONST.LED.COLS, CONST.LED.ROWS)
    for idx, one_list in enumerate(led_array):
        if idx % 2 != 0:
            led_array[idx] = list(reversed(one_list))
    # RGB_DICT
    led_id = 0
    for one_list in list(led_array.T):
        for idx in one_list:
            new_rgb_dict[idx] = rgb_dict[led_id]
            led_id += 1
    return new_rgb_dict
