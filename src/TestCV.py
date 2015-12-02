import numpy as np
import cv2
 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
vc = cv2.VideoCapture(0)
rval, img = vc.read()

if rval == False:
    exit()

while 1 > 0:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
 
    cv2.imshow('img',img)
    rval, img = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyAllWindows()
