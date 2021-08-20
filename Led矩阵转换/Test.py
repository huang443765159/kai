import cv2
import numpy as np


def rbg_mapping(one_frame: list):
    pixel_dict = dict()
    new_pixel_dict = dict()
    addr = 0
    for pixels in one_frame:
        for pixel in pixels:
            pixel_dict[addr] = pixel
            addr += 1
    # for idx, rgb in enumerate(rgb_list):
    #     rgb_dict[idx] = rgb
    led = [i for i in range(80 * 120)]
    led_array = np.array(led).reshape(80, 120)
    print(led_array)
    for idx, one_list in enumerate(led_array):
        if idx % 2 != 0:
            led_array[idx] = list(reversed(one_list))
    # RGB_DICT
    print(led_array.T)
    for idx, p_id in enumerate(led_array.T.reshape(1, 80 * 120).tolist()[0]):
        new_pixel_dict[p_id] = pixel_dict[idx]
    return sorted(new_pixel_dict.items())


if __name__ == '__main__':
    img = cv2.imread('5.jpeg')
    img = cv2.resize(img, (80, 120))
    frame = rbg_mapping(one_frame=np.array(img).tolist())
