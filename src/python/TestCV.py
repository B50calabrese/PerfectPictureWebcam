import numpy as np
import cv2
 
vc = cv2.VideoCapture(0)

WIDTH = 640
HEIGHT = 480

def getImg():
  _,i = vc.read()
  #res = cv2.resize(i,[WIDTH, HEIGHT], fx = .5, fy = .5, interpolation = cv2.INTER_AREA)
  return i

lowerArray = np.array([50, 100, 100], np.uint8)
upperArray = np.array([70, 255, 255], np.uint8)

img = getImg()

while 1 > 0:
    print "Converting to green"
    greenImg = cv2.inRange(img, lowerArray, upperArray)
    print "Finding contours"
    contours,h = cv2.findContours(greenImg, 1, 2)
    print "Printing contours"
    for cnt in contours:
      approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
      if len(approx) == 4:
        print "Found green square!!!!", cnt
    input a
    img = getImg()
vc.release()
