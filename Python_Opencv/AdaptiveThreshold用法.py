import cv2
from matplotlib import pyplot as plt

# 第一个参数：原图，第二个参数：要变成的值，第三个参数：阈值方法，第四个参数：阈值取值的方法，第五个参数：计算阈值的区域大小，第六个参数：常数
# 返回值：一个(image)
# cv2.ADPTIVE_THRESH_MEAN_C：阈值取自相邻区域的平均值
# cv2.ADPTIVE_THRESH_GAUSSIAN_C：阈值取值相邻区域的加权和，权重为一个高斯窗口。


img1 = cv2.imread('black.jpg', 0)
# img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
thresh2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh3 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img1, thresh1, thresh2, thresh3]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# cv2.imshow('IMG', thresh1)
plt.show()

if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
