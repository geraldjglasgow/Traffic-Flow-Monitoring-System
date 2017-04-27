iwconfig - ifconfig

Man page: http://manpages.ubuntu.com/manpages/zesty/en/man8/iwconfig.8.html

Configure WiFi and wireless card settings, useful link:
https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

Command used to bring down a WiFi interface:

> sudo ifconfig wlan0 down

Command used to bring up a WiFi interface:

> sudo ifconfig wlan0 up

Command used to set WiFi interface to monitor mode:

> sudo iwconfig wlan1 mode Monitor
