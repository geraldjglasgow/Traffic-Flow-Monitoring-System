This is a spike on how to have program run on RPi startup

Here is a good like for starters:
https://www.raspberrypi.org/documentation/linux/usage/rc-local.md

This command brings up a file, where any command you put above the 'exit 0' at the bottom of the file 
will be run while the RPi is starting up
> sudo nano /etc/rc.local

Below are some useful commands to use while setting up the pi for the first time

* change default time:
> sudo dpkg-reconfigure tzdata
* to change RPi to 12 hour clock, right click the clock and go to change digital clock settings, and change the %R to %r
* to change default keyboard:
> sudo vim /etc/default/keyboard

change XKBLAYOUT="gb" to XKBLAYOUT="us" (for USA standard keyboard)


