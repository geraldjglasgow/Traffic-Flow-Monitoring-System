import RPi.GPIO as GPIO
import time as t 

# This program will use a button connected to GND and a GPIO pin, to wait for 
# a button push, which can trigger an event


pin = 18 # GPIO pin being used for button
GPIO.setmode(GPIO.BCM)  
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

while True:
    try:  
        GPIO.wait_for_edge(pin, GPIO.FALLING)
	# do something on button press
	# no need to sleep (not pulling)
        
    except KeyboardInterrupt:
        #catch/log error
