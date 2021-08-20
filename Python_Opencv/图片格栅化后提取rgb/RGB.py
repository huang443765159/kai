import cv2
import numpy as np


src = cv2.imread('img.png')
rows, cols, channels = src.shape  # 行，列， rgb
src_cpy = src.copy()

rect = dict()
rect['x'] = 100
rect['y'] = 250
rect['width'] = 10
rect['height'] = 10

select_image = src_cpy[rect['y']:rect['y'] + rect['height'], rect['x']:rect['x'] + rect['width']]
# 150： 160， 100： 110
# print(src_cpy, select_image)
cv2.rectangle(src, (rect['x'], rect['y']), (rect['x'] + rect['width'], rect['y'] + rect['height']), (255, 0, 0), 3)
# print(select_image)
# cv2.imshow('org', src)

for y in range(rows):
    for x in range(cols):
        x_mid = int(x / rect['width']) * rect['width'] + int(rect['width'] / 2)
        # print("x {}=>{}".format(x, x_mid))
        y_mid = int(y / rect['height']) * rect['height'] + int(rect['height'] / 2)
        # print("y {}=>{}".format(y, y_mid))
        # ret, thresh1 = cv2.threshold(src_cpy, 180, 255, cv2.THRESH_BINARY)
        src_cpy[y][x] = src_cpy[int(y_mid)][int(x_mid)]

b, g, r = cv2.split(src_cpy)
print('b', len(b))
# print('g', g)
# print('r', r)
# cv2.imshow('b', b)
# cv2.imshow('g', g)
cv2.imshow('r', r)

# cv2.imshow('1img', src_cpy)
cv2.waitKey()
cv2.destroyAllWindows()
