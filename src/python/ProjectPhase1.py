import RPi.GPIO as GPIO
import time
import cv2

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
leftPosition = 0.078
rightPosition = 0.061

msPerCycle = 20

sleepTime = .15

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
    else:
        pwm2.start(key)
        time.sleep(sleepTime)
        pwm2.stop()

pwm1.stop()
pwm2.stop()
GPIO.cleanup()
