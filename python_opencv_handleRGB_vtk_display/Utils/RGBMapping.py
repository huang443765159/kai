import numpy as np


def rgb_mapping(rgb_list):
    rgb_dict = dict()
    new_rgb_dict = dict()
    for idx, rgb in enumerate(rgb_list):
        rgb_dict[idx] = rgb
    points = [i for i in range(64 * 150)]
    new_points = np.array(points).reshape(64, 150)
    for idx, one_list in enumerate(new_points):
        if idx % 2 != 0:
            new_points[idx] = list(reversed(one_list))
    p_id = 0
    for one_list in list(new_points.T):
        for idx in one_list:
            new_rgb_dict[idx] = rgb_dict[p_id]
            p_id += 1
    return new_rgb_dict
