import cv2
from matplotlib import pyplot as plt
# 第一个参数：原图， 第二个参数：阈值， 第三个参数：高于或者低于阈值后要变成的值， 第四个参数：阈值方法
# 返回值：2个，第二个是返回的image

img = cv2.imread('img.png')
img1 = cv2.imread('图片黑白反转/2.png', 0)  # 使用阈值必须先转灰
# img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)  # 127以下：黑， 127以上：白
print(thresh1)
ret, thresh2 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV)  # 127以下L：白，127以上：黑
ret, thresh3 = cv2.threshold(img1, 127, 255, cv2.THRESH_TRUNC)  # 127以下：不变，127以上：白
ret, thresh4 = cv2.threshold(img1, 127, 255, cv2.THRESH_TOZERO)  # 127以下：黑， 127以上：灰
ret, thresh5 = cv2.threshold(img1, 127, 255, cv2.THRESH_TOZERO_INV)  # 127以下：灰， 127以上：黑
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img1, thresh1, thresh2, thresh3, thresh4, thresh5]

# for i in range(6):
#     plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

# cv2.imshow('IMG', thresh1)
# plt.show()

cv2.imwrite('1.jpg', thresh1)
if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()