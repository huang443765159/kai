from hyperlpr import *
import cv2


class CarNumRecognition(object):

    def __init__(self, image_path, video_path):
        self._image_path = image_path
        self._video_path = video_path

    def video(self):
        print('[INFO] starting video stream')
        stream = cv2.VideoCapture(self._video_path)
        while 1:
            grabbed, frame = stream.read()
            if not grabbed:
                print('NO DATA')
                break
            res = HyperLPR_plate_recognition(frame)
            print(res)
            key = cv2.waitKey(5) & 0xFF
            if key == ord('q'):
                break
            stream.release()
            cv2.destroyAllWindows()

    def image(self):
        print('[INFO] starting image')
        image = cv2.imread(self._image_path)
        res = HyperLPR_plate_recognition(image)
        print(res)


if __name__ == '__main__':

    _video = '/Users/huangkai/Desktop/test.mp4'
    _image = '/Users/huangkai/Desktop/1.png'

    _test = CarNumRecognition(video_path=_video, image_path=_image)
    _test.video()
    # _test.image()
