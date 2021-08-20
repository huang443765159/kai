import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('black.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
# 膨胀
dil = cv2.dilate(img, kernel, iterations=1)
# 腐蚀
ero = cv2.erode(dil, kernel, iterations=1)
# 开运算：先膨胀再腐蚀，去除噪声
_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# 闭运算：先腐蚀再膨胀 填补前景物上的洞或者黑点
_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# 前景物体的轮廓
_grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# 原图像与进行开运算后的图像的差
_top = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# 原图像与进行闭运算后的图像的差
_black = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
# cv2.imshow('pig', ero)
# cv2.imshow('dil', dil)
# cv2.imshow('org', img)
# cv2.imshow('open', _open)
# cv2.imshow('close', _close)
# cv2.imshow('drad', _grad)
cv2.imshow('black', _black)
# cv2.imshow('top', _top)
cv2.waitKey(0)
cv2.destroyAllWindows()
