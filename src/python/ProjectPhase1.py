import RPi.GPIO as GPIO
import time
import cv2

def moveUp():
  dutyCyclePercentage = leftPosition * 100 / msPerCycle
  pwm1.start(dutyCyclePercentage)
  time.sleep(sleepTime)
  pwm1.stop()

def moveDown():
  dutyCyclePercentage = rightPosition * 100 / msPerCycle
  pwm1.start(dutyCyclePercentage)
  time.sleep(sleepTime)
  pwm1.stop()
  
def moveLeft():
  dutyCyclePercentage = leftPosition * 100 / msPerCycle
  pwm2.start(dutyCyclePercentage)
  time.sleep(sleepTime)
  pwm2.stop()

def moveRight():
  dutyCyclePercentage = rightPosition * 100 / msPerCycle
  pwm2.start(dutyCyclePercentage)
  time.sleep(sleepTime)
  pwm2.stop()

sleepTime = 0.05

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
leftPosition = 0.75
rightPosition = 2.5

msPerCycle = 1000 / frequencyHertz

done = False

key = 'a'

while not done:
    
    key = raw_input("Input:")

    if key == 'w':
        moveUp()
    elif key == 's':
        moveDown()
    elif key == 'a':
        moveLeft()
    elif key == 'd':
        moveRight()
    elif key == 'q':
        done = True

pwm1.stop()
pwm2.stop()
GPIO.cleanup()
