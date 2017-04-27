sleep 30
sudo ifconfig wlan0 down
sleep 3
sudo iwconfig wlan0 mode Monitor
sleep 3
sudo ifconfig wlan0 up
sleep 3
cd /home/pi/path to probemon.py
sleep 2
sudo python probemon.py -i wlan0 -r -t unix
