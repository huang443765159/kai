import time
import socket
import imagezmq
from imutils.video import VideoStream


sender = imagezmq.ImageSender(connect_to='tcp://192.168.50.151:5555')
rpi_name = socket.gethostname()
pi_cam = VideoStream(usePiCamera=True).start()
time.sleep(2)
while 1:
    image = pi_cam.read()
    print(image)
    # sender.send_image(rpi_name, image)
