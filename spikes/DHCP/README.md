# Spike for DHCP.<br />
To transfer files from the raspberry pi to a computer via ad-hoc a dhcp server is needed to
make the process easier, so the client doesn't have to assign their own IP address and netmask.

To download an easy to use dhcp server use:

> sudo apt-get install isc-dhcp-server

Next, the interface the ad-hoc network is hosted needs to be specified. Here I specify wlan0

> sudo nano /etc/default/isc-dhcp-server<br />
> INTERFACES="wlan0" 

Now the dhcpd.conf file needs to be configured. <br />
Below is a good example of what it should look like.
 	
> sudo nano /etc/dhcp/dhcpd.conf

DHCPDARGS=wlan0;<br />
default-lease-time 600;<br />
max-lease-time 7200;<br />
 
option subnet-mask 255.255.255.0;<br />
option broadcast-address 10.0.0.255;<br />
option domain-name "RPi-network";<br />
option routers 10.0.0.1; #default gateway<br />
 
subnet 10.0.0.0 netmask 255.255.255.0 { <br />
    range 10.0.0.2 10.0.0.10; <br />
}


 /* this is for static IP addresses */ <br />
host myLaptop { 
    hardware ethernet aa:aa:aa:aa:aa:aa;
    fixed-address 10.0.0.100;
}

Lastly if you don't want dhcp server to run at boot use this command:
> sudo update-rc.d -f isc-dhcp-server remove

To start dhcp manually use this command:
> /usr/sbin/dhcpd wlan0
