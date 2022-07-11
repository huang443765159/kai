import cv2
import socket
import pickle
import base64
import numpy as np


network = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

frame = cv2.imread('B.jpeg')
tx_data = pickle.dumps((b'\x01', frame))

head, rx_data = pickle.loads(tx_data)
print(head, rx_data)
# cv2.imshow('1', rx_data)
# cv2.waitKey(0)
