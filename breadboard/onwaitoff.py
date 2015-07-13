import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

# TODO: use sys.argv to set the on, off, and repeat variables

# turn LED on for a set time, the off for a set time

def flickon(on_secs, off_secs, repeat):

    counter = 0

    while counter < repeat:

        # turn LED on
        GPIO.output(17, GPIO.HIGH)

        # wait while light is on
        time.sleep(on_secs)

        # turn LED off
        GPIO.output(17, GPIO.LOW)

        # wait while LED is off
        time.sleep(off_secs)

        counter += 1  # add 1 to counter


flickon(0.05, 0.05, 100)

print "Finished the light show"




