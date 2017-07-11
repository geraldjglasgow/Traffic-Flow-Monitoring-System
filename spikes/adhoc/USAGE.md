When the r-pi starts up a script will be run to automatically host an ad-hoc network.
If a known client doesn't try to connect within 2 minutes, then the r-pi will switch to 
monitor mode and begin logging traffic.

If a specific client connects to the network within the couple minutes, then the ad-hoc network 
will persist as long as the client is connected.

This will also require the computer has a manual ip address set to talk with the rpi over adhoc.
below is the command to set an ip and netmask

To check the current IP use:
> sudo ipconfig getifaddr <interface>


> sudo ifconfig <interface> 192.168.1.2 netmask 255.255.255.0

The interface for integrated wireless cards will be en0 for mac and wlan0 for linux.
