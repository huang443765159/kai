from matplotlib import pyplot as plt
import numpy as np
import cv2

# 直方图的 x 轴是灰度值（0 到 255），y 轴是图片中具有同一个灰度值的点的数目。
# cv2.calcHist(images,channels,mask,histSize,ranges[,hist[,accumulate]])
# 1. images: 原图像（图像格式为 uint8 或 float32）。当传入函数时应该用中括号 [] 括起来，例如：[img]。
# 2. channels: 同样需要用中括号括起来，它会告诉函数我们要统计那幅图像的直方图。如果输入图像是灰度图，它的值就是 [0]；
#    如果是彩色图像的话，传入的参数可以是 [0]，[1]，[2] 它们分别对应着通道 B，G，R。
# 3. mask: 掩模图像。要统计整幅图像的直方图就把它设为 None。但是如果你想统计图像某一部分的直方图的话，你就需要制作一个掩模图像，并使用它
# 4. histSize:BIN 的数目。也应该用中括号括起来，例如：[256]。
# 5. ranges: 像素值范围，通常为 [0，256]

img = cv2.imread('/Users/huangkai/Desktop/black.jpg')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()
