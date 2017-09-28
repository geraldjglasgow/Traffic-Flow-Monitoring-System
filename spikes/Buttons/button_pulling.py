import RPi.GPIO as GPIO
import time

# Program checks every .2 seconds if the button has been pressed. This method uses a lot of CPU time and power

pin = 18
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(pin)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)