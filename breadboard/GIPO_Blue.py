__author__ = 'ambell'

import RPi.GPIO as GPIO  # Import library that lets you control the Pi's GPIO pins
from time import sleep  # Import time for delays

GPIO.setwarnings(False)  # Disables messages about GPIO pins already being in use
GPIO.setmode(GPIO.BOARD)  # Indicates which pin numbering configuration to use

pinNumLED = 7
pinNumBTN = 16
GPIO.setup(pinNumLED, GPIO.OUT)  # Tells it that pinNumLED will be outputting
GPIO.setup(pinNumBTN, GPIO.IN)  # Tells it that pinNumBTN will be giving input

## Initialize btnOn and prev_input
btnOn = False
prev_input = 1

print "press button"

while btnOn is False:
    try:
        input = GPIO.input(pinNumBTN)

        if ((not prev_input) and input):
            btnOn = not btnOn
        prev_input = input
        sleep(0.05)

        ## When the button is pressed, start toggling the LED between
        ## HIGH and LOW with a 0.5s interval between
        if btnOn:
            print "button on"
            GPIO.output(pinNumLED, PIO.HIGH)
            sleep(0.5)
            GPIO.output(pinNumLED, GPIO.LOW)
            sleep(0.5)
        else:
            print "button off"
            GPIO.output(pinNumLED, GPIO.HIGH)

    except KeyboardInterrupt:
        break
