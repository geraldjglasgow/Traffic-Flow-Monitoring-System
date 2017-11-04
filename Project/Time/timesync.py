import os
import time as t
import subprocess

# sudo hwclock -r will display the current system time
# sudo hwclock -s will set the system time from the RTC
# sudo hwclock -w will set the RTC from system time

# updates system time every 2 minutes
while True:
	p = subprocess.Popen(["sudo hwclock -s"], stdout=subprocess.PIPE, shell=True)
	# out = p.stdout.read()
	# print(out.decode('ascii'))
	t.sleep(120)
