import cv2
import numpy as np

# cap = cv2.VideoCapture("rtsp://burak:123456@192.168.1.92/user=burak&password=123456&channel=1&stream=1.sdp?")
# cap = cv2.VideoCapture("rtsp://burak:123456@192.168.1.92:554/user=burak&password=123456&channel=1&stream=0.sdp?")
print("başladı")

cap = cv2.VideoCapture("rtsp://burak:123456@192.168.1.59:554/user=burak_password=123456_channel=6_stream=0.sdp?real_stream")





print("biti")
while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("tamam")