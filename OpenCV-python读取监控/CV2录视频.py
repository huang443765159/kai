
import cv2

cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # frame = cv2.flip(frame, 0)  # 反转
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()  # Release everything if job is finished
out.release()
cv2.destroyAllWindows()
