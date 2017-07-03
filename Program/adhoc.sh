sleep 30
sudo ifconfig wlan0 down
sleep 2
sudo ifconfig wlan1 down
sleep 5
sudo iwconfig wlan1 channel 1 essid Pi mode ad-hoc
sleep 3
ifconfig wlan1 192.168.1.1 netmask 255.255.255.0
sleep 3
sudo ifconfig wlan1 up
