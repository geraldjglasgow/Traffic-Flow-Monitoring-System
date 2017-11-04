run sudo nano /etc/default/isc-dhcp-server
change to INTERFACES="wlan0"

run sudo nano /etc/dhcp/dhcpd.conf

DHCPDARGS=wlan0;
default-lease-time 600;
max-lease-time 7200;

option subnet-mask 255.255.255.0;
option broadcast-address 10.0.0.255;
option domain-name "Traffic Pi1";
option routers 10.0.0.1;

subnet 10.0.0.0 netmask 255.255.255.0 {
        range 10.0.0.2 10.0.0.10;
}

host Macbook {
        hardware ethernet 9c:f3:87:b5:ad:fa;
        fixed-address 10.0.0.100;
}
