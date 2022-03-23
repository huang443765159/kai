import cv2
# opencv读取图像
img = cv2.imread('1.png', 1)
cv2.imshow('img', img)
img_shape = img.shape  # 图像大小(565, 650, 3)
print(img_shape)
h = img_shape[0]
w = img_shape[1]
# 彩色图像转换为灰度图像（3通道变为1通道）
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
# 最大图像灰度值减去原图像，即可得到反转的图像
dst = 255 - gray
cv2.imshow('dst', dst)  # 只能在主线程imshow，子线程会报错
cv2.imwrite('2_2.png', dst)
cv2.waitKey(0)
