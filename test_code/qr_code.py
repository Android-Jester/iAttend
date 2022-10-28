import cv2
import numpy as np
from pyzbar.pyzbar import *


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    thickness = 2
    rect_thickness = 1
    for qr_code in decode(frame):
        data = qr_code.data.decode('utf-8')
        pts = np.array([qr_code.polygon], np.int)
        rect = np.array([qr_code.rect], np.int)
        pts = pts.reshape((-1, 1, 2))
        print(data) 
        # cv2.polylines(frame, [pts], True,(255,255,0),1)
        for x,y,w,h in rect:
            w , h =x+w, y+h
            cv2.rectangle(frame, (x,y), (w,h), (255,255,0), rect_thickness)

            cv2.line(frame,(x,y),(x+15,y),(255,255,0),thickness)
            cv2.line(frame,(x,y),(x,y+15),(255,255,0),thickness)

            cv2.line(frame,(w,y),(w-15,y),(255,255,0),thickness)
            cv2.line(frame,(w,y),(w,y+15),(255,255,0),thickness)

            cv2.line(frame,(x,h),(x+15,h),(255,255,0),thickness)
            cv2.line(frame,(x,h),(x,h-15),(255,255,0),thickness)

            cv2.line(frame,(w,h),(w-15,h),(255,255,0),thickness)
            cv2.line(frame,(w,h),(w,h-15),(255,255,0),thickness)
                   
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()