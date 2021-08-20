import cv2
import numpy as np
import time

img = cv2.imread('black.jpg')
img1 = cv2.imread('1.png')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([30, 30, 30])
upper_blue = np.array([255, 255, 255])
mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
# 参数介绍  hsv_image, 阈值范围低值：图片中低于这个值的变为0， 阈值范围高值：图片中高于这个值的变为0
res = cv2.bitwise_and(img, img, mask=mask)


cv2.imshow('IMG', res)


if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
