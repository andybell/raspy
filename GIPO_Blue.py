__author__ = 'ambell'

import RPi.GPIO as GPIO ## Import library that lets you control the Pi's GPIO pins
from time import sleep # Import time for delays
from ISStreamer.Streamer import Streamer ## Import the Initial State streamer

## Streamer constructor, this will create a bucket called Button Blink
## you'll be able to see this name in your list of logs on initialstate.com
## your access_key is a secret and is specific to you, don't share it!
streamer = Streamer(bucket="Button Blink", access_key="[Your Access Key Here]")

GPIO.setwarnings(False) ## Disables messages about GPIO pins already being in use
GPIO.setmode(GPIO.BOARD) ## Indicates which pin numbering configuration to use

pinNumLED = 7
pinNumBTN = 16
GPIO.setup(pinNumLED,GPIO.OUT) ## Tells it that pinNumLED will be outputting
GPIO.setup(pinNumBTN,GPIO.IN) ## Tells it that pinNumBTN will be giving input

## Initialize btnOn and prev_input
btnOn = False
prev_input = 1

## Stream a message when the button is ready to press
streamer.log("msg","Press the Button!")

while True:
    try:
        input = GPIO.input(pinNumBTN)

        if ((not prev_input) and input):
            btnOn = not btnOn
        prev_input=input
        sleep(0.05)

        ## When the button is pressed, start toggling the LED between
        ## HIGH and LOW with a 0.5s interval between
        if btnOn:
            GPIO.output(pinNumLED,GPIO.HIGH)
            streamer.log("LED","Off") ## Stream that the LED is Off
            sleep(0.5)
            GPIO.output(pinNumLED,GPIO.LOW)
            streamer.log("LED","On") ## Stream that the LED is On
            sleep(0.5)
        else:
            GPIO.output(pinNumLED,GPIO.HIGH)


    except KeyboardInterrupt:
        break

## Stream a message when the loop has been broken
streamer.log("msg","Finished!")
streamer.close()