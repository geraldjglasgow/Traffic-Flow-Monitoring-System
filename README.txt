The spikes folder contains information on the individule componets of our system,
as well as tools that are used or were potential candidates for use.

Hardware requirements:
- Raspberry Pi 2 model B with Rasbian Jessie installed
- network card that supports Monitor and Adhoc modes (tested with Alfa AWUS051NH v.2)
- 3 push buttons
- Powerboost 1000c
- 3.7V LiPo battery
- Powerbank that supports 5V 1A output
- Direction Antenna
- DS3231 RTC
- Weather-proof case to hold all parts


Below is all the steps required to setup this project to monitor vehical
traffic using WiFi probe requests on a raspberry pi with Raspbian Jessi.

1. You can either download the files from the repository or clone it.
  - to clone make sure you have git installed
  > sudo apt-get install update
  > sudo apt-get install git
  
  - go to or create the directory you want to code to go into and use this command
  > git clone git@github.com:geraldjglasgow/Traffic-monitoring-with-WiFi-data.git
  - move the Project folder to the pis home directory

2. install the required libraries

 > sudo apt-get install python-pip
 > sudo apt-get install python-scapy
 > sudo apt-get install trash-cli
 
3. 
  > sudo nano /etc/rc.local
  - add this paths to the line above 'exit 0'
  > /home/pi/Project/Buttons/start.py &
  > /home/pi/Project/Buttons/start.py &
  > /home/pi/Project/Buttons/start.py &
  
4. Lastly, make sure I2C and SSH is enabled
  > In terminal type in: 
  > sudo raspi-config
  > go to option 5 and enabled the I2C and SSH
  
