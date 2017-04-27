Wireshark and tshark - 

TShark is a network protocol analyzer. It lets you capture packet data from a live network, or read packets from a previously saved capture file, either printing a decoded form of those packets to the standard output or writing the packets to a file. TShark's native capture file format is pcap format, which is also the format used by tcpdump and various other tools.

Wireshark lets you see what’s happening on your network at a microscopic level and is the de facto standard across many commercial and non-profit enterprises, government agencies, and educational institutions. 

Using either of these programs with the .pcap file output from kismet it’s possible to use filters to obtain and safe the output needed. In this case the filter was wlan.fc.type_subtype==0x04 filter was used to only display the probe requests detected and these requests can be later analyzed. 

Here is the command to install tshark in linux:
 > sudo apt-get install tshark

