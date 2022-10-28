import cv2
import face_recognition


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_recognition.face_locations(gray)
    thickness = 2
    rect_thickness = 1
    color = (255,255,0)
    print(face)
    for (left,bottom,right,top) in face:
        
        cv2.rectangle(frame, (top,left), (bottom,right), color, rect_thickness)

        cv2.line(frame,(top,left),(top+15,left),color,thickness)
        cv2.line(frame,(top,left),(top,left+15),color,thickness)

        cv2.line(frame,(bottom,left),(bottom-15,left),color,thickness)
        cv2.line(frame,(bottom,left),(bottom,left+15),color,thickness)

        cv2.line(frame,(top,right),(top+15,right),color,thickness)
        cv2.line(frame,(top,right),(top,right-15),color,thickness)

        cv2.line(frame,(bottom,right),(bottom-15,right),color,thickness)
        cv2.line(frame,(bottom,right),(bottom,right-15),color,thickness)
              

    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()