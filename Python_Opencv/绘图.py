import cv2
import numpy as np

img = cv2.imread('black.jpg')
# 图片， 左上角坐标，右下角坐标， 颜色，线宽
cv2.line(img, (0, 0), (350, 511), (255, 0, 0), 5)
# 图片， 圆点， 半径， 颜色，线宽
cv2.circle(img, (250, 63), 63, (0, 0, 255), -1)  # -1 代表实心
# 图片， 圆点， 半径， 旋转角度， 椭圆启始角度， 椭圆结束角度， 颜色，线宽-实心
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, (0, 255, 0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
# 图片，要添加的文字， 坐标， 字体， 字体大小， 颜色， 字体线条宽度
cv2.putText(img, 'zuo', (100, 480), font, 4, (255, 0, 0), 2)
cv2.imshow('line', img)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
