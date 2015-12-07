# Gives control of the GPIO pins on the raspberry pi.
import RPi.GPIO as GPIO

# Used for time delays.
import time

# Used for key input.
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

done = False

key = 'a'

while not done:
    
    key = raw_input("Input:")

    if key == 'w':
        dutyCyclePercentage = leftPosition * 100 / msPerCycle
        pwm.start(dutyCyclePercentage)
        time.sleep(.5)
    elif key == 's':
        dutyCyclePercentage = rightPosition * 100 / msPerCycle
        pwm.start(dutyCyclePercentage)
        time.sleep(.5)
    elif key == 'q':
        done = True

pwm.stop()

GPIO.cleanup()
