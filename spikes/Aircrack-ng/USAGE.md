Aircrack-ng has tools available for easily creating an interface for wireless cards to be put into 'monitor mode'. 

Linux users can install using:
> sudo apt-get install aircrack-ng

Once installed and your monitor mode capable wireless card is plugged in,
this command can be used to see the wireless interfaces.
> iwconfig

Output similar to this should be displayed.

> eth0 no wireless extensions.

> wlan0 IEEE 802.11bgn ESSID: "something"
> Mode: Managed Frequency: 2.437Ghz Access Point: ff:ff:ff:ff:ff:ff
> Bit Rate=72.2Mb/s  Tx-Powre=17dBm


If your device doesn't have wifi capability then wlan0 will the the plugged in wireless card.
If your device already has wifi capability, then wlan0 will be the integrated card and wlan1 
will be the wireless card.

Next well setup a monitor mode interface with this command

> sudo airmon-ng [start|stop|check] [interface]

Example: 
> sudo airmon-ng start wlan1

If the wireless card can be put into monitor mode then it should display
a device named mon0 when >iwconfig is ran again. If not the wireless card
is not compatable with aircrack-ng.

> eth0 no wireless extensions.

> mon0 IEEE 802.11bgn Mode: Monitor Tx-Powre=20dBm
> Retry short limit:7 RTS thr=2347 B Fragment thr:off
> Power Management:on

> wlan0 IEEE 802.11bgn Mode: Managed Tx-Powre=20dBm
> Retry short limit:7 RTS thr=2347 B Fragment thr:off
> Power Management:on

to remove an interface created by airmon-ng you can use the stop flag

Example: 
> sudo airmon-ng stop mon0
