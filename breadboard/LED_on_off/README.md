# Turn LED on and off using python

## Original source
On/off LED from https://youtu.be/R6s_7UaOSKA

## Requires
 - breadboard
 - t-connector
 - LED
 - resistor (TODO: which type?)
 - jumper cable

## Breadboard Layout
Place LED in breadboard so legs are in two different rows. Connect jumper cable from GIPO # 17 to the row with LED's long leg, then connect the resistor from row with the LED's short leg to the -3v column.

![](layout_1.JPG?raw=true)
![](layout_2.JPG?raw=true)

## Usage

sudo python on.py -> turns LED on

sudo python off.py -> turns LED off

sudo python onoffrepeat.py on_secs off_secs repeat_times -> turns LED on for an set ammount of time, then off for a set ammount of time and then repeats for x times.
