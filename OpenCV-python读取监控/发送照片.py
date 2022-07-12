import cv2
import socket
import pickle
import base64
import numpy as np


network = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

frame = cv2.imread('B.jpeg')
new_frame = cv2.resize(frame, (int(frame.shape[1] * 0.2), int(frame.shape[0] * 0.2)))
tx_data = pickle.dumps((b'\x01', new_frame))
print(len(tx_data))

head, rx_data = pickle.loads(tx_data)
new_rx = cv2.resize(rx_data, (int(rx_data.shape[1] * 2), int(rx_data.shape[0] * 2)))
# print(head, rx_data)
cv2.imshow('1', new_rx)
cv2.waitKey(0)
