import RPi.GPIO  as g
import time as t
from time import gmtime, strftime
import os

g.setmode(g.BCM)
g.setup(21,g.IN,pull_up_down=g.PUD_UP)

while True:
	file = open("/home/pi/Project/Battery/battery.log","a")
	if g.input(21) == g.LOW:
		file.write(strftime("%Y-%m-%d %I:%M:%S"))
		file.write(" Low\n")
		file.close()
		os.system('sudo shutdown -h now')
	else:
		file.write(strftime("%Y-%m-%d %I:%M:%S"))
		file.write(" High\n")
		t.sleep(60)