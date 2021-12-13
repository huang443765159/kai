from hyperlpr import *
import cv2


class CarNumRecognize(object):

    def __init__(self):
        pass

    def recognize(self):
        cap = cv2.VideoCapture(0)
        print(f'IP摄像头是否开启：{cap.isOpened()}')
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        frame_count = 1
        while 1:
            grabbed, frame = cap.read()
            if not grabbed:
                print('NO DATA')
                break
            else:
                frame_count += 1
                if frame_count % 5 == 0:
                    frame_count = 0
                    res = HyperLPR_plate_recognition(frame)
                    if res:
                        car_num, confidence, rect = res[0]
                        print(f'车牌：{car_num}, 置信度：{confidence}, 坐标： {rect}')
                    # cv2.imshow('Window', frame)
                key = cv2.waitKey(10) & 0xFF
                if key == 27:
                    cap.release()
                    break
            # cv2.destroyAllWindows()


if __name__ == '__main__':
    _test = CarNumRecognize()
    _test.recognize()
