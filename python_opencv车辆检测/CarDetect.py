import cv2


class CarDetect(object):

    def __init__(self, video_path, image_path):
        self._video_path = video_path
        self._image_path = image_path
        self._car_cascade = cv2.CascadeClassifier('file.xml')

    def video_detect(self):
        cap = cv2.VideoCapture(self._video_path)
        cv2.namedWindow('Video')
        while 1:
            ret, frame = cap.read()
            if ret:
                frame = cv2.resize(frame, (320, 240))
                gary_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                car = self._car_cascade.detectMultiScale(gary_frame, 1.3, 5, cv2.CASCADE_SCALE_IMAGE)
                if len(car):
                    image = cv2.cvtColor(gary_frame, cv2.COLOR_GRAY2BGR)
                    for x, y, w, h in car:
                        cv2.rectangle(image, (x, y), (x+w, y+h), (155, 230, 180), 2)
                    cv2.imshow('video', image)
                    if cv2.waitKey(20) & 0xff == ord('q'):
                        cap.release()
                        cv2.destroyAllWindows()
                        break
            else:
                cap.release()
                cv2.destroyAllWindows()
                break

    def image_detect(self):
        image = cv2.imread(self._image_path, 0)
        car = self._car_cascade.detectMultiScale(image, 1.3, 5, cv2.CASCADE_SCALE_IMAGE)
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        print(car)
        if len(car):
            for x, y, w, h in car:
                cv2.rectangle(image, (x, y), (x+w, y+h), (155, 230, 180), 2)
            cv2.imshow('image', image)
            if cv2.waitKey(0) & 0xff == ord('q'):
                cv2.destroyAllWindows()


if __name__ == '__main__':
    _video_path = 'cars.mp4'
    _image_path = 'color.png'
    _car = CarDetect(video_path=_video_path, image_path=_image_path)
    # _car.image_detect()
    _car.video_detect()
