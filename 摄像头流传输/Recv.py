import cv2
import imagezmq


# 只能在同局域网下

image_hub = imagezmq.ImageHub()
while 1:
    rpi_name, image = image_hub.recv_image()
    cv2.imshow(rpi_name, image)
    cv2.waitKey(1)
    image_hub.send_reply(b'ok')
    print('ok')
