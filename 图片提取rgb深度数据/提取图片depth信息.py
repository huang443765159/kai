import os
import cv2
import numpy as np

img = 'Fire.jpeg'
img_ori = cv2.imread(img, -1)
depth = cv2.split(img_ori)[0]
depth[depth > 2000] = 0
depth = depth / 2000
cv2.imshow('img', depth)
cv2.waitKey(0)
