import cv2
import numpy as np
#import RPi.GPIO as GPIO
import time

def moveUp():
  dutyCyclePercentage = leftPosition
  #pwm1.start(dutyCyclePercentage)
  time.sleep(sleepTime)
  print "Moving up"
  #pwm1.stop()

def moveDown():
  dutyCyclePercentage = rightPosition
  #pwm1.start(dutyCyclePercentage)
  time.sleep(sleepTime)
  print "Moving down"
  #pwm1.stop()
  
def moveLeft():
  dutyCyclePercentage = leftPosition
  #pwm2.start(dutyCyclePercentage)
  time.sleep(sleepTime)
  print "Moving left"
  #pwm2.stop()

def moveRight():
  dutyCyclePercentage = rightPosition
  #pwm2.start(dutyCyclePercentage)
  time.sleep(sleepTime)
  print "Moving right"
  #pwm2.stop()

def decideMovement(x1, y1, x2, y2):
  epsilon = 100
  print x1," ",y1," ",x2," ",y2
  if (x1 > x2 + epsilon):
    moveLeft()
  elif (x1 + epsilon < x2):
    moveRight()
  if (y1 > y2 + epsilon):
    moveUp()
  elif (y1 + epsilon < y2):
    moveDown()
  
def main():
    vc = cv2.VideoCapture(0)
    _, img = vc.read()
    minArea = 30
    height, width, n = img.shape
    centerImgX = width / 2
    centerImgY = height / 2
    # Used to grab only the green pixels in an HSV image.
    lowerArray = np.array([160, 100, 100], np.uint8)
    upperArray = np.array([179, 255, 255], np.uint8)

    while True:
        # Blur the image to reduce noise.
        blur = cv2.blur(img, (5,5))

        # Convert the image to hsv.
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        # Conver the image to only red.
        redImg = cv2.inRange(hsv, lowerArray, upperArray)

        # Find the contours in the image.
        contours,hierarchy = cv2.findContours(redImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
          approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

          # If it is a square.
          if len(approx) == 4 and cv2.contourArea(cnt) > minArea:
            x,y,w,h = cv2.boundingRect(cnt)
            decideMovement(centerImgX, centerImgY, x + (w / 2), y + (h / 2))
            cv2.drawContours(img, [cnt], -1, (0, 255, 0), 3)

        #cv2.imshow('img', img)
        _, img = vc.read()
        key = cv2.waitKey(10)
        if key == 27:
          break
    cv2.destroyAllWindows()

  
# Global values and constants.
outputPin1 = 12
outputPin2 = 11
leftPosition = 10.0
rightPosition = 50
msPerCycle = 20
sleepTime = .01
frequencyHertz = 90

# Set the mode for indexing pins.
#GPIO.setmode(GPIO.BOARD)

# Tells the CPU which pins do what.
#GPIO.setup(outputPin1, GPIO.OUT)
#GPIO.setup(outputPin2, GPIO.OUT)
#pwm1 = GPIO.PWM(outputPin1, frequencyHertz)
#pwm2 = GPIO.PWM(outputPin2, frequencyHertz)

main()

#pwm1.stop()
#pwm2.stop()
#GPIO.cleanup()
