When looking at microcontrollers there are a few things to consider. Does it have enough power to quickly capture hundreds of thousands of packets while looking for just the probe requests, does it support a wireless card that supports monitor mode, and finally  how much power does the card use.

Most small TI and arduino controllers do not provide sufficient processing power to capture the maximum amount of packets possible. In addition most require the use of a select few of wireless cards that don’t support monitor mode. Knowing this the raspberry pi was a suitable option. After testing the RPi 1,2,3, and zero, the RPi zero meets our needs of being powerful enough to capture many packets, supports many wireless cards that support monitor mode, and is power efficient.

In the future the use of one of TI's CM3200 controllers might be an option to cut down on power consumption if a suitable wireless card can be used with it.
