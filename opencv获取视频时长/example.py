import cv2

cap = cv2.VideoCapture('test.mp4')
if cap.isOpened():
    rate = cap.get(5)
    frame = cap.get(7)
    duration = frame / rate
    print(duration)
