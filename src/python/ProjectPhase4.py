import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

def quickPulse(pinNumber):
  GPIO.output(pinNumber, 1)
  time.sleep(sleepTime)
  GPIO.output(pinNumber, 0)

def moveRight():
  print "Right"
  quickPulse(clockwisePin)

def moveLeft():
  print "Left"
  quickPulse(counterclockwisePin)
  
def moveDown():
  print "Down"
  return

def moveUp():
  print "Up"
  return

def decideMovement(x1, y1, x2, y2):
  epsilon = 50
  if (x1 > x2 + epsilon):
    moveLeft()
    return True
  elif (x1 + epsilon < x2):
    moveRight()
    return True
  if (y1 > y2 + epsilon):
    moveUp()
    return True
  elif (y1 + epsilon < y2):
    moveDown()
    return True
  return False
  
def main():
    vc = cv2.VideoCapture(0)
    _, img = vc.read()
    minArea = 120
    height, width, n = img.shape
    centerImgX = width / 2
    centerImgY = height / 2
    # Used to grab only a certain set of pixels in an HSV image.
    lowerArray1 = np.array([160, 80, 100], np.uint8)
    upperArray1 = np.array([179, 255, 255], np.uint8)
    lowerArray2 = np.array([0, 80, 100], np.uint8)
    upperArray2 = np.array([10, 255, 255], np.uint8)

    while True:
	# Blur the image to reduce noise.
        blur = cv2.blur(img, (5,5))

        # Convert the image to hsv.
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        # Conver the image to only red.
        redImg1 = cv2.inRange(hsv, lowerArray1, upperArray1)
        redImg2 = cv2.inRange(hsv, lowerArray2, upperArray2)
        redImg = cv2.addWeighted(redImg1, 1.0, redImg2, 1.0, 0.0)

        # Find the contours in the image.
        contours,hierarchy = cv2.findContours(redImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        moved = False

        for cnt in contours:
          approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
          area = cv2.contourArea(cnt)
          print area
          # If it is a rectanle.
          if len(approx) == 4 and area > minArea:
            x,y,w,h = cv2.boundingRect(cnt)
            print x," ", y
            moved = decideMovement(centerImgX, centerImgY, x + (w / 2), y + (h / 2))
            cv2.drawContours(img, [cnt], -1, (0, 255, 0), 3)
          if moved:
            break

        cv2.imshow('img', img)
        _, img = vc.read()
        key = cv2.waitKey(10)
        if key == 27:
          break
    cv2.destroyAllWindows()

  
# Global values and constants.
clockwisePin = 11
counterclockwisePin = 12
sleepTime = .2

# Set the mode for indexing pins.
GPIO.setmode(GPIO.BOARD)

# Tells the CPU which pins do what.
GPIO.setup(clockwisePin, GPIO.OUT)
GPIO.setup(counterclockwisePin, GPIO.OUT)

# main()

while True:
  moveRight()
  time.sleep(.5)
  moveLeft()
  time.sleep(.5)

GPIO.cleanup()
