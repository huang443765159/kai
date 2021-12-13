import cv2


class Camera(object):

    def __init__(self, width, height):
        self._cap = cv2.VideoCapture(0)  # 0代表自带的摄像头，1代表外部摄像头， 也可以打开ip摄像头/usb摄像头
        # 摄像头的IP地址,http://用户名：密码@IP地址：端口/
        # ip_camera_url = 'http://admin:admin@192.168.1.101:8081/'
        # cap = cv2.VideoCapture(ip_camera_url)
        print('IP摄像头是否开启： {}'.format(self._cap.isOpened()))
        if not self._cap.isOpened():
            self._cap.release()
        # SET CAMERA
        self._cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self._cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self._working()

    def _working(self):
        while 1:
            ret, frame = self._cap.read()  # 第一个参数返回一个布尔值（True/False），代表有没有读取到图片；第二个参数表示截取到一帧的图片
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 转灰度图
            cv2.imshow('img', gray)
            cv2.imshow('Window', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self._cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    test = Camera(1280, 960)
