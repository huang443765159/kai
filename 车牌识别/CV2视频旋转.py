import numpy as np
import cv2

cap = cv2.VideoCapture('/Users/huangkai/Desktop/test.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi', fourcc, 20.0, (1280, 1080))  # 视频输出名字。 编码格式， 帧率， 视频输出大小

while 1:
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 0)  # 视频反转
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
