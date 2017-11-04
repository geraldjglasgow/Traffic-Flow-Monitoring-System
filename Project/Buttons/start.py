import RPi.GPIO as GPIO
import time as t
import os
import datetime as dt

pin = 17
GPIO.setmode(GPIO.BCM)  
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def run():  
	os.system('sudo service isc-dhcp-server stop')
	os.system('sudo ifconfig wlan0 down')
	os.system('sudo iwconfig wlan0 mode Monitor')
	os.system('sudo ifconfig wlan0 up')
	os.system("cd /home/pi/Project/Battery\nsudo python battery.py &")
	os.system("cd /home/pi/Project/Temperature\nsudo python cpu.py &")
	os.system("cd /home/pi/Project/probe-finder\nsudo python probemon.py &")
	#os.system('cd /home/pi/Project\ntshark -i wlan0 -f "subtype probereq" -F pcap -w "output.pcap" &')
	#os.system("cd /home/pi/Project\nbluelog -i hci0 -t -a 0")
	
def main():
	while True:
		try:
			GPIO.wait_for_edge(pin, GPIO.FALLING)
			file = open("button.log","a")
			file.write("Log Probes Pressed: %s\n" % str(t.strftime("%m/%d/%Y %I:%M:%S")))
			file.close()
			t.sleep(2)
			run()
		except KeyboardInterrupt:
			file = open("button.log", "a")
			file.write("Log Probes Error: %s\n" % str(t.strftime("%m/%d/%Y %I:%M:%S")))
			file.close()

if __name__ == "__main__":
	main()