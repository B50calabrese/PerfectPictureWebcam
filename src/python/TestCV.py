import numpy as np
import cv2
 
vc = cv2.VideoCapture(0)

WIDTH = 640
HEIGHT = 480

def getImg():
  _,i = vc.read()
  #res = cv2.resize(i,[WIDTH, HEIGHT], fx = .5, fy = .5, interpolation = cv2.INTER_AREA)
  return i

img = getImg()

while 1 > 0:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,threshold = cv2.threshold(gray, 127, 255, 1)
    print "Finding contours"
    contours,h = cv2.findContours(threshold, 1, 2)
    print "Printing contours"
    for cnt in contours:
      approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
      if len(approx) == 4:
        print "Found square!!!!", cnt
    img = getImg()
vc.release()
