Wireshark and tshark - 
Using either of these programs with the .pcap file output from kismet it’s possible to use filters to obtain and safe the output needed. In this case the filter was wlan.fc.type_subtype==0x04 filter was used to only display the probe requests detected and these requests can be later analyzed. 

