import RPi.GPIO as GPIO
import time as t
import os
import datetime as dt

pin = 27
GPIO.setmode(GPIO.BCM)  
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

def adhoc():
    os.system('sudo killall python')
    os.system('sudo ifconfig wlan0 down')
    os.system('sudo iwconfig wlan0 mode ad-hoc')
    os.system('sudo iwconfig wlan0 essid "Traffic Pi1"')
    os.system('sudo iwconfig wlan0 key "s:apple"')
    os.system('sudo ifconfig wlan0 10.0.0.201 netmask 255.255.255.0')
    os.system('sudo ifconfig wlan0 up')
    os.system("cd /usr/sbin\nsudo dhcpd wlan0")
    
def main():
	while True:
    		try:  
        		GPIO.wait_for_edge(pin, GPIO.FALLING)
        		file = open("button.log", "a")
        		file.write("Adhoc Pressed: %s\n" % str(t.strftime("%m/%d/%Y %I:%M:%S")))
        		file.close()
        		t.sleep(2)
        		adhoc()
    		except KeyboardInterrupt:
        		file = open("log.txt", "a")
        		file.write("Adhoc Error: %s\n" % str(t.strftime("%m/%d/%Y %I:%M:%S")))
        		file.close()

if __name__ == "__main__":
	main()
