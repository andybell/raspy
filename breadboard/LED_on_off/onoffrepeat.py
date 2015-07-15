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

try:

    # enter number of seconds as command line arguements (on_seconds, off_seconds, repeat_value)
    flickon(float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))

    print "Finished the light show"

except:
    print "Something caused the light show to quit unexpectedly."
    
    if len(sys.argv) != 4:
        print "Make sure you supplied the right parameters: seconds on, seconds off, number times to repeat"

    # in case of error make sure lights turn off
    GPIO.output(17, GPIO.LOW)

