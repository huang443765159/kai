import cv2
from hyperlpr import *


def video():
    print('[INFO] starting video stream')
    stream = cv2.VideoCapture('/Users/huangkai/Desktop/test.mp4')
    while 1:
        grabbed, frame = stream.read()
        if not grabbed:
            print(' NO DATA')
            break
        # cv2.imshow('Frame', frame)
        res = HyperLPR_plate_recognition(frame)
        print(res)
        cv2.putText(frame, str(res), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 255), 2)
        key = cv2.waitKey(5) & 0xFF
        if key == ord('q'):
            break
        stream.release()


def image():
    print('[INFO] starting image')
    _image = cv2.imread('/Users/huangkai/Desktop/1.jpg')
    res = HyperLPR_plate_recognition(_image)
    print(res)


if __name__ == '__main__':
    # video()
    image()
    cv2.destroyAllWindows()
