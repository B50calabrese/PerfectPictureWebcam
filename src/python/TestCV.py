import numpy as np
import cv2
 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
vc = cv2.VideoCapture(0)
rval, img = vc.read()
font = cv2.FONT_HERSHEY_SIMPLEX

if rval == False:
    exit()

while 1 > 0:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    # Puts text on the image, the text being "Test". The position is (10, 500).
    # The text size is 4. The color is white. The scale is 2, and always use
    # cv2.LINE_AA.
    cv2.putText(img, "Test", (10,500), font, 4, (255,255,255), 2, cv2.LINE_AA)
    cv2.imshow('img',img)
    rval, img = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyAllWindows()
vc.release()
