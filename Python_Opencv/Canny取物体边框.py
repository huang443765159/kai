import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('black.jpg', 0)
blur = cv2.GaussianBlur(img, (5, 5), 0)
edges = cv2.Canny(img, 50, 300)
# 图片 阈值1， 阈值2， 低于阈值1的被抛弃，高于阈值2的为边界，然后在阈值1-2之间的点会和距离最近的边界连接
print(edges)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
# 练习
# 1. 写一个小程序，可以通过调节滑动条来设置阈值 minVal 和 maxVal 进而来进行 Canny 边界检测。这样你就会理解阈值的重要性了。
