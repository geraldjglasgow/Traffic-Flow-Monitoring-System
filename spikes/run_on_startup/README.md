This is a spike on how to auto run programs on the raspberry pi

Here is a good like for starters:
https://www.raspberrypi.org/documentation/linux/usage/rc-local.md

For this project specifically we need to automate the wireless card interfacing to monitor mode.
This is only possible through running a bash script (seen in programs) to delay the script till startup, 
run commands to put the card in monitor mode, then start the program.

below are commands for putting card in monitor mode:

	> sudo ifconfig wlan0 down
	> sudo iwconfig wlan0 mode Monitor
	> sudo ifconfig wlan0 up

Once this is finished you must cd to the directory that contains probemon.py file

 > cd /home/pi/path to probemon.py file

Once at the right directory its time to run the program:

	> sudo python probemon.py -i wlan0 -r -t unix

You can choose the flags you wish for running the program.
