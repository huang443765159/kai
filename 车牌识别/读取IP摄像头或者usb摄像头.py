'''
Opencv-python读取IP摄像头视频流/USB摄像头
'''

import cv2

# 创建一个窗口 名字叫做Window
cv2.namedWindow('Window', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)

'''
#打开USB摄像头
cap = cv2.VideoCapture(0)
'''

# 摄像头的IP地址,http://用户名：密码@IP地址：端口/
# ip_camera_url = 'http://admin:admin@192.168.1.101:8081/'
# 创建一个VideoCapture
# cap = cv2.VideoCapture(ip_camera_url)
cap = cv2.VideoCapture(0)

print('IP摄像头是否开启： {}'.format(cap.isOpened()))

# 显示缓存数
print('缓存', cap.get(cv2.CAP_PROP_BUFFERSIZE))
# 设置缓存区的大小
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

# 调节摄像头分辨率
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 设置FPS
print('setfps', cap.set(cv2.CAP_PROP_FPS, 25))
print(cap.get(cv2.CAP_PROP_FPS))

while 1:
    # 逐帧捕获
    ret, frame = cap.read()  # 第一个参数返回一个布尔值（True/False），代表有没有读取到图片；第二个参数表示截取到一帧的图片
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Window', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 当一切结束后，释放VideoCapture对象
cap.release()
cv2.destroyAllWindows()
