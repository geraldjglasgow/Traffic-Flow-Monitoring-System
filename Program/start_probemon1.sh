sleep 30
sudo ifconfig wlan0 down
sleep 2
sudo ifconfig wlan1 down
sleep 5
sudo iwconfig wlan1 mode Monitor
sleep 3
sudo ifconfig wlan1 up
sleep 3
cd /home/pi/path to probemon.py
sleep 2
sudo python probemon.py -i wlan1 -r -t unix
