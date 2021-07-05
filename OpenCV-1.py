import cv2
import numpy as np
print(cv2.__version__)
print(np.__version__)


# webcam
cam = cv2.VideoCapture('/dev/video1')

# RPi Camera
# camSet = 'nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1, format=NV12 ! nvvidconv flip-method=2 ! video/x-raw, width=800, height=600, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink drop=1'
# cam = cv2.VideoCapture(camSet)


while True:
    _, frame = cam.read()
    fps = cam.get(cv2.CAP_PROP_FPS)
    print(fps)
    cv2.imshow('frame', frame)
    cv2.moveWindow('frame', 0 , 0)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
