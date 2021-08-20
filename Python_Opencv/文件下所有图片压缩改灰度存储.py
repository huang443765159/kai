import cv2
import os

# 方法一 缺点：必须先把文件下照片改成按顺序排列的，却在for里面必须包含照片的名字
path = '/Users/huangkai/Desktop/2/'
# for i in range(1, 9):
#     print(path + str(i) + '.jpg')
#     img = cv2.imread(path + str(i) + '.jpg', 0)
#     res_img = cv2.resize(img, (50, 50), interpolation=cv2.INTER_LANCZOS4)
#     cv2.imwrite('/Users/huangkai/Desktop/3/' + os.sep + str(i) + '.png', res_img)

# 方法二 比较灵活，推荐使用
files = os.listdir(path)
print(files)
n = 0
for file in files:
    img = cv2.imread(path + file)
    res_img = cv2.resize(img, (300, 300), interpolation=cv2.INTER_LANCZOS4)
    cv2.imwrite('/Users/huangkai/Desktop/' + str(n + 1) + '.jpg', res_img)
    n += 1
