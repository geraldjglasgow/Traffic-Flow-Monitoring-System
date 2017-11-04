import RPi.GPIO as GPIO
import time as t
import os
import datetime as dt

pin = 23
GPIO.setmode(GPIO.BCM)  
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

def main():
	while True:
    		try:  
        		GPIO.wait_for_edge(pin, GPIO.FALLING)
        		file = open("button.log", "a")
        		file.write("Shutdown Pressed: %s\n" % str(t.strftime("%m/%d/%Y %I:%M:%S")))
        		file.close()
        		t.sleep(2)
        		os.system('sudo shutdown -h now')
    		except KeyboardInterrupt:
        		file = open("log.txt", "a")
        		file.write("Shutdown Error: %s\n" % str(t.strftime("%m/%d/%Y %I:%M:%S")))
        		file.close()

if __name__ == "__main__":
	main()
