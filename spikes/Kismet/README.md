Kismet is a program that has lots of features, including the one we need, which is logging packets. It was ultimately not
chosen as the packet logger for this project, but can still be used and is very easy to setup.
The setup for kismet involves either downloading or compiling the program and configuring it.

Here is the commands to install the latest version on linux:

> sudo apt-get update 
> sudo apt-get install kismet

There is a .conf file in /usr/local/etc called kismet.conf. You will need to edit this for the program to work.
Inside kismet.conf, #ncsource=wlan0 will need to be uncommented as this specifies the wireless interface being used.
The path to save output will need to be redifined if desired. This is visible when first editing the file and looks like
logprefix=/usr/local/etc

Once the wireless card is in monitor mode and the .conf file has the interface specified one can run kismet by typing “kismet” in terminal. It’s not recommended to run kismet as sudo, and there is very good documentation to show to to run kismet properly as a user. Once running in the defined path for output will hold the output files for kismet.
