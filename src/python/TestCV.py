# Gives control of the GPIO pins on the raspberry pi.
import RPi.GPIO as GPIO

# Used for time delays.
import time
import numpy as np
import cv2
 
# The pin that we will be using to control the servo.
outputPin = 12

# Tell Pi which pin numbers we'll be using to refer to the GPIO pins.
# This is the actual physical pin ordering on the board.
GPIO.setmode(GPIO.BOARD)

# Tells the CPU which pins do what.
GPIO.setup(outputPin, GPIO.OUT)

frequencyHertz = 90
pwm = GPIO.PWM(outputPin, frequencyHertz)

# Position values.
leftPosition = 0.75
rightPosition = 2.5

msPerCycle = 1000 / frequencyHertz
 
vc = cv2.VideoCapture(0)

def rotateLeft():
  dutyCyclePercentage = leftPosition * 100 / msPerCycle
  pwm.start(dutyCyclePercentage)
  time.sleep(.1)
  pwm.stop

def rotateRight():
  dutyCyclePercentage = rightPosition * 100 / msPerCycle
  pwm.start(dutyCyclePercentage)
  time.sleep(.1)
  pwm.stop()

def getImg():
  _,i = vc.read()
  return i

# Used to grab only the green pixels in an HSV image.
lowerArray = np.array([50, 100, 100], np.uint8)
upperArray = np.array([70, 255, 255], np.uint8)

img = getImg()
height, width, n = img.shape
height = height / 2
width = width / 2
a = 'w'
while 1 > 0:
    # Blur image in order to reduce noise.
    blur = cv2.blur(img, (5,5))
 
    print "Converting to green"
    
    # Converts the image to HSV then grabs only the green.
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    greenImg = cv2.inRange(hsv, lowerArray, upperArray)
    
    print "Finding contours"
    
    contours,h = cv2.findContours(greenImg, 1, 2)
    
    print "Printing contours"
    
    count = 1
    centerX = width
    centerY = height
    
    for cnt in contours:
      approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
      if len(approx) == 4:
        x,y,w,h = cv2.boundingRect(cnt)
        centerX = centerX + (x + w / 2)
        centerY = centerY + (y + h / 2)
    centerX = centerX / count
    centerY = centerY / count
    
    if (centerX < width):
      rotateLeft()
    if (centerX > width):
      rotateRight()
    
    a = raw_input()
    if a == 'q':
      break
    img = getImg()
vc.release()
