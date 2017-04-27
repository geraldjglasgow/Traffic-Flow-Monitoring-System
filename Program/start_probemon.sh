 #!/bin/bash

echo "Hello World"
sudo ifconfig wlan0 down
echo "wlan0 down"
sudo ifconfig wlan1 down
echo "wlan1 down"
sudo iwconfig wlan1 mode Monitor
echo "wlan1 Monitor mode"
sudo ifconfig wlan1 up
echo "wlan1 up"
cd ../..
cd Desktop/probemon-master
echo "Starting probemon"
sudo python probemon.py -i wlan1 -f
