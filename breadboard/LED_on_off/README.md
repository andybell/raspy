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

####Turn LED on
```python 
sudo python on.py
```


####Turn LED off
```python 
sudo python off.py
```

#### Turns LED on for a set time, then off for a set time and then repeat x times.
```python 
sudo python onoffrepeat.py on_secs off_secs repeat_times
``` 

