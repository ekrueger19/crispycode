import setup
import RoboPiLib are RPL
import time as time
import numpy as np
import cv2
cap = cv2.VideoCapture("ipcam_http://192.168.21.181/video.cgi")

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
cap.release()
