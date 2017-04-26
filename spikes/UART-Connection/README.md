In order to access the pi easily it is recommended to enable and use ssh or simply connect a UART to the pi. 

On a linux machine:

This command displays all connected usb devices. Make sure one of them is a serial usb device.
> lsusb 

This command will display the serial usb connecter. 
> ls -l /dev/ttyUSB0

To access the pi through serial usb just type this command
> sudo screen /dev/ttyUSB0 115200 

The pi should prompt you for login credentials. 
Default credentials are
user: pi
password: raspberry
