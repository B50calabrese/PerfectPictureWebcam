import RPi.GPIO as GPIO
import time
import numpy as np
import cv2
import curses

def moveUp():
  dutyCyclePercentage = leftPosition
  pwm1.start(dutyCyclePercentage)
  time.sleep(sleepTime)
  pwm1.stop()

def moveDown():
  dutyCyclePercentage = rightPosition
  pwm1.start(dutyCyclePercentage)
  time.sleep(sleepTime)
  pwm1.stop()
  
def moveLeft():
  dutyCyclePercentage = leftPosition
  pwm2.start(dutyCyclePercentage)
  time.sleep(sleepTime)
  pwm2.stop()

def moveRight():
  dutyCyclePercentage = rightPosition
  pwm2.start(dutyCyclePercentage)
  time.sleep(sleepTime)
  pwm2.stop()
  
def savePicture():
  vc = cv2.VideoCapture(0)
  _,img = vc.read()
  cv2.imwrite(fileName, img)

fileName = "saved_pic.jpeg"

# The pins that we will be using to control the servos.
outputPin1 = 12
outputPin2 = 11

# Tell Pi which pin numbers we'll be using to refer to the GPIO pins.
# This is the actual physical pin ordering on the board.
GPIO.setmode(GPIO.BOARD)

# Tells the CPU which pins do what.
GPIO.setup(outputPin1, GPIO.OUT)
GPIO.setup(outputPin2, GPIO.OUT)

frequencyHertz = 90
pwm1 = GPIO.PWM(outputPin1, frequencyHertz)
pwm2 = GPIO.PWM(outputPin2, frequencyHertz)

# Position values.
leftPosition = 10.0
rightPosition = 50

msPerCycle = 20

sleepTime = .2

done = False

key = 'a'

val = 0.0

# Initialize various things for curses to work.
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

while key != ord('q'):
    
    key = stdscr.getch()
    stdscr.addch(20, 25, key)
    stdscr.refresh();
    if key == ord('w'):
        moveUp()
    elif key == ord('s'):
        moveDown()
    elif key == ord('a'):
        moveLeft()
    elif key == ord('d'):
        moveRight()
    elif key == ord('p'):
        savePicture()
curses.endwin()
pwm1.stop()
pwm2.stop()
GPIO.cleanup()
