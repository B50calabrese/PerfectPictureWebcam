# Gives control of the GPIO pins on the raspberry pi.
import RPi.GPIO as GPIO

# Used for time delays.
import time

# Used for key input.
import cv2

#def set(property, value):
#  f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
#  f.write(value)
#  f.close()

# The pin that we will be using to control the servo.
outputPin = 12

# Tell Pi which pin numbers we'll be using to refer to the GPIO pins.
# This is the actual physical pin ordering on the board.
GPIO.setmode(GPIO.BOARD)

# Tells the CPU which pins do what.

GPIO.setup(outputPin, GPIO.OUT)

#set("delayed", "0")
#set("mode", "servo")
#set("servo_max", 180)
#set("active", 1)

delay_period = 1

frequencyHertz = 90
pwm = GPIO.PWM(outputPin, frequencyHertz)


# Position values.
leftPosition = 0.75
rightPosition = 2.5

msPerCycle = 1000 / frequencyHertz

done = False

counter = 0.0

pwm.start()
time.sleep(.02)
pwm.stop()

#while not done:
#    set("servo", str(counter))
#    time.sleep(delay_period)
#    pwm.start(counter)
#    time.sleep(.1)
#    pwm.stop()
#    counter = counter + 1
#    if (counter >= 180.0):
#      break

GPIO.cleanup()
