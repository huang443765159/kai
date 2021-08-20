import cv2

# 函数 cv2.findContours() 有三个参数，
# 第一个是输入图像，第二个是轮廓检索模式，第三个是轮廓近似方法。
# 返回值有三个，第一个是图像，第二个是轮廓，第三个是（轮廓的）层析结构。
# 轮廓（第二个返回值）是一个 Python列表，其中存储这图像中的所有轮廓。每一个轮廓都是一个 Numpy 数组，包含对象边界点（x，y）的坐标。
# 注意：我们后边会对第二和第三个参数，以及层次结构进行详细介绍。在那之前，例子中使用的参数值对所有图像都是适用的。
#
#
# 21.1.2 怎样绘制轮廓
# 函数 cv2.drawContours() 可以被用来绘制轮廓。它可以根据你提供的边界点绘制任何形状。
# 它的第一个参数是原始图像，第二个参数是轮廓，一个 Python 列表。第三个参数是轮廓的索引（在绘制独立轮廓是很有用，当设置为 -1 时绘制所有轮廓）
# 接下来的参数是轮廓的颜色和厚度等。


im = cv2.imread('2.jpg', 0)  # 灰图
ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)  # 二值化
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 找出轮廓
img = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)  # 转彩色
img1 = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)  # 画轮廓
cv2.imshow('show', img1)
# cv2.imwrite('black_line.png', img1)

if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
