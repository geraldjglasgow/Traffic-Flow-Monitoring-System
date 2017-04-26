Aircrack-ng has tools available for easily creating an interface for wireless cards to be put into 'monitor mode'. 

Linux users can install using:
> sudo apt-get install aircrack-ng

Once installed and your monitor mode capable wireless card is plugged in,
this command can be used to see the wireless interfaces.
> iwconfig

Output similar to this should be displayed.





If your device doesn't have wifi capability then wlan0 will the the plugged in wireless card.
If your device already has wifi capability, then wlan0 will be the integrated card and wlan1 
will be the wireless card.

Next well setup a monitor mode interface with this command

> sudo airmon-ng [start|stop|check] [interface]


<h1> this is h1 </h1>
this is normal
