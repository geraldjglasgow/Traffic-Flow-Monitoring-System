The spikes folder contains information on the individule componets of our system,
as well as tools that are used or were potential candidates for use.


Below is all the steps required to setup this project to monitor vehical
traffic using WiFi probe requests.

1. You can either download the files from the repository or clone it.
  - to clone make sure you have git installed
  > sudo apt-get install update
  > sudo apt-get install git
  
  - go to or create the directory you want to code to go into and use this command
  > git clone git@github.com:geraldjglasgow/Traffic-monitoring-with-WiFi-data.git

2. install the required libraries

 > sudo apt-get install python-pip
 > sudo pip install netaddr
 > sudo apt-get install python-scapy
 > sudo apt-get install tcpdumb
 
3. to auto run the program on startup 
  > sudo nano /etc/rc.local
  
