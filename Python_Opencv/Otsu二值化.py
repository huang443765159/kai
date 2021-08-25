import cv2
import numpy as np
from matplotlib import pyplot as plt

#  这里用到到的函数还是 cv2.threshold()
#  但是需要多传入一个参数（flag）：cv2.THRESH_OTSU。这时要把阈值设为 0。然后算法会找到最优阈值，这个最优阈值就是返回值 retVal
#  如果不使用 Otsu 二值化，返回的retVal 值与设定的阈值相等。
#  高斯模糊降噪后二值化效果是最好的， ret2/ret3是二值化的最优阈值


# img = cv2.imread('image.jpg', 0)
img = cv2.imread('图片黑白反转/1.png', 0)
# cv2.imshow('IMG4', img)
# cv2.imwrite('IMG1.png', img)
# img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret1, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(img, (3, 3), 0)
ret3, thresh3 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3]
print(ret1, ret2, ret3)

# for i in range(4):
#     plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

cv2.imshow('IMG1', thresh1)
cv2.imshow('IMG2', thresh2)
cv2.imshow('IMG3', thresh3)
cv2.imwrite('PigPeng.png', thresh3)
# plt.show()

if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()