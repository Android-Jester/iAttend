import os
import cv2
import numpy as np
import face_recognition
from datetime import datetime

path = "test_code\\images"
images = []

image_list = os.listdir(path)

def get_names(images: list, image_list: list, path: str):
    names = []
    for item in image_list:
        current_image = cv2.imread(f'{path}/{item}')
        images.append(current_image)
        names.append(os.path.splitext(item)[0])
    return names

name_list = get_names(images, image_list, path)

def get_encodings(images):
    encodings_list = []
    for image in images:
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encode_face = face_recognition.face_encodings(image)[0]
        encodings_list.append(encode_face)
    return encodings_list

encode_list=get_encodings(images)

def mark_attendance(name):
    with open(r'test_code\\attendance.csv', 'r+') as f:
        data = f.readlines()
        namelist = []
        for line in data:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            h = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{h}')
     


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    curent_frame_face = face_recognition.face_locations(gray)
    curent_frame_encode = face_recognition.face_encodings(frame,num_jitters=1,model="small")
    fps = 1/30
    thickness = 2
    rect_thickness = 1
    color = (255,255,0)
    fps = int(fps * 1000)
    print("fps: ", fps)
    for encode_face, face_location in zip(curent_frame_encode, curent_frame_face):
        (left,bottom,right,top) = face_location
        cv2.rectangle(frame, (top,left), (bottom,right), (255,255,0), rect_thickness)
        cv2.line(frame,(top,left),(top+15,left),color,thickness)
        cv2.line(frame,(top,left),(top,left+15),color,thickness)
        cv2.line(frame,(bottom,left),(bottom-15,left),color,thickness)
        cv2.line(frame,(bottom,left),(bottom,left+15),color,thickness)
        cv2.line(frame,(top,right),(top+15,right),color,thickness)
        cv2.line(frame,(top,right),(top,right-15),color,thickness)
        cv2.line(frame,(bottom,right),(bottom-15,right),color,thickness)
        cv2.line(frame,(bottom,right),(bottom,right-15),color,thickness)

        matches = face_recognition.compare_faces(encode_list, encode_face)
        face_distance = face_recognition.face_distance(encode_list, encode_face)
        match_index = np.argmin(face_distance)
        if matches[match_index]:
            get_name = name_list[match_index].upper()
            mark_attendance(get_name)
            (left,bottom,right,top) = face_location
            cv2.rectangle(frame, (top,left), (bottom,right), (255,255,0), rect_thickness)
            print(get_name)
        elif not  matches[match_index]:
            print("No matches found")
            pass
            
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()