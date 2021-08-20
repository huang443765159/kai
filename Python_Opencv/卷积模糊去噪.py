import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('/Users/huangkai/Desktop/black.jpg')

kernel = np.ones((5, 5), np.float32)/25  # 平均滤波器的核
dst = cv2.filter2D(img, -1, kernel)  # 平均滤波器
plt.subplot(121), plt.imshow(img), plt.title('Ori')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('fil')
plt.xticks([]), plt.yticks([])
plt.show()


# 方法二
blur = cv2.blur(img, (5, 5))  # 等同于平均模糊，可直接使用
cv2.imshow('blur', blur)

# 方法三 高斯模糊
blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow('gauss', blur)

if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
