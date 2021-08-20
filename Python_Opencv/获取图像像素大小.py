import cv2
import numpy as np

img = cv2.imread('black.jpg')
px = img[50, 50]  # 坐标50, 50点的像素
red = img[50, 50, 2]  # 返回是一个列表，2代表列表里第三个值 等同于img[50, 50][2]
# 修改某个点的像素
img[100, 100] = [255, 255, 255]
# 获取图像形状
shape = img.shape
# 获取图像像素
size = img.size
# 获取图像数据类型
_type = img.dtype
cv2.imshow('black', img)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
