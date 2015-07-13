import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)


# turn LED on for a second, the off for a second

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


flickon(2, 0.5, 10)

print "Finished the light show"




