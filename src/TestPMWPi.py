# Gives control of the GPIO pins on the raspberry pi.
import RPi.GPIO as GPIO

# Used for time delays.
import time

# The pin that we will be using to control the servo.
outputPin = 11

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
middlePosition = (rightPosition - leftPosition) / 2 + leftPosition

positionList = [leftPosition, middlePosition, rightPosition, middlePosition]

msPerCycle = 1000 / frequencyHertz

# Iterate through the positions sequence 3 times.
for i in range(3):
    for position in positionList:
        dutyCyclePercentage = position * 100 / msPerCycle
        print "Position: " + str(position)
        print "Duty Cycle: " + stry(dutyCyclePercentage) + "%"
        print ""
        pwm.start(dutyCyclePercentage)
        time.sleep(.5)

pwm.stop()

GPIO.cleanup()
