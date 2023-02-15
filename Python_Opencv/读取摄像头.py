import cv2

video = cv2.VideoCapture(1)
fps = video.get(cv2.CAP_PROP_FPS)
print(fps)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)
video.set(3, 500)  # 高
video.set(4, 400)  # 宽
while True:
    ret, frame = video.read()
    cv2.imshow("A video", frame)
    c = cv2.waitKey(1)
    if c == 27:
        break
video.release()
