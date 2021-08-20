import cv2
# detectMultiScale参数介绍
"""
1.image表示的是要检测的输入图像，转灰后加快处理速度

2.objects表示检测到的人脸目标序列

3.scaleFactor表示每次图像尺寸减小的比例

4. minNeighbors表示每一个目标至少要被检测到3次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸),

5.minSize为目标的最小尺寸

6.minSize为目标的最大尺寸
返回值是左上角启始坐标，宽，高
"""
# rectangle参数介绍
"""
1.image表示检测到的图像
2.（x, y）矩形左上角
3.（x+w， x+h）矩形右下角
4.（0， 255， 0）矩形颜色
5.矩形线宽
"""

cascade = cv2.CascadeClassifier('/Users/huangkai/Documents/opencv-3.4.3/data/haarcascades_cuda/h'
                                'aarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cv2.namedWindow('Camera')
while 1:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (680, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = cascade.detectMultiScale(gray, 1.3, 5)
        for x, y, w, h in face:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow('Camera', frame)
        if cv2.waitKey(5) & 0xff == ord('q'):
            cap.release()
            break

cv2.destroyAllWindows()
