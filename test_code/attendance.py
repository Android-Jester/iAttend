import os
import cv2
import numpy as np
import face_recognition


imageElon = face_recognition.load_image_file(r'test_code\\images\\elon.jpg')
imageElon = cv2.cvtColor(imageElon, cv2.COLOR_BGR2RGB)

elon_test = face_recognition.load_image_file(r'test_code\\images\\elon.jpg')
elon_test = cv2.cvtColor(elon_test, cv2.COLOR_BGR2RGB)

face_loc = face_recognition.face_locations(imageElon)[0]
face_end = face_recognition.face_encodings(imageElon)[0]

face_test = face_recognition.face_encodings(elon_test)[0]

cv2.rectangle(imageElon, (face_loc[3],face_loc[0]), (face_loc[1],face_loc[2]), (255,255,0), 1)
cv2.rectangle(elon_test, (face_loc[3],face_loc[0]), (face_loc[1],face_loc[2]), (255,255,0), 1)

results = face_recognition.compare_faces([face_end],face_test )
distance = face_recognition.face_distance([face_end],face_test )

print(face_end.ndim)

# cv2.imshow('img',imageElon)
# cv2.imshow('img_1',elon_test)
cv2.waitKey(0)

