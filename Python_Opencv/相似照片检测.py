from skimage.metrics import structural_similarity
import imutils
import numpy as np
import cv2


img1 = cv2.imread('2.jpg', 0)
img2 = cv2.imread('6.jpg', 0)
(score, diff) = structural_similarity(img1, img2, full=True)
diff = (diff * 255).astype('uint8')
# cv2.imshow('diff', diff)
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[1] if imutils.is_cv3() else cnts[0]
img2 = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
for c in cnts:
    if len(c):
        print(True)
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img1, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0), 2)
    else:
        print(False)
cv2.imshow('modifieed', img1)
cv2.imshow('haha2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
注意事项：比对照片尺寸必须一致， 如果物体在照片中的位置不一致，则打印出False
"""
# 方法二， 每一寸像素判定，只要有一点不一样就会返回false
img1 = cv2.imread('6.jpg')
img2 = cv2.imread('t5.jpg')
diff = cv2.subtract(img1, img2)  # 把每一格的像素相减
result = not np.any(diff)  # 有一点不一样都会返回false
print(result)

# 方法三，直方图判定,返回的是相似度
img1_hist = cv2.calcHist([img1], [1], None, [256], [0, 256])
img1_hist = cv2.normalize(img1_hist, img1_hist, 0, 1, cv2.NORM_MINMAX, -1)

img2_hist = cv2.calcHist([img2], [1], None, [256], [0, 256])
img2_hist = cv2.normalize(img2_hist, img2_hist, 0, 1, cv2.NORM_MINMAX, -1)
similar = cv2.compareHist(img1_hist, img2_hist, 0)
print(similar)
