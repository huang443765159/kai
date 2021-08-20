import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('img.png', 0)
blur = cv2.GaussianBlur(img, (3, 3), 0)
ret, image = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(ret)
# blur1 = cv2.blur(blur, (5, 5))
kernel = np.ones((2, 2), np.uint8)
# ero = cv2.erode(image, kernel, iterations=1)
gra = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# cv2.imshow('IMG2', img)
cv2.imshow('IMG3', gra)
cv2.imwrite('zzcimg.png', gra)
# plt.show()

if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
