#!/usr/bin/python
import datetime
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # suppresses IPV6 Error
from scapy.all import *


NAME = 'probemon'
INTERFACE = 'wlan0'
logger = logging.getLogger(NAME)

def get_probes(packet):
        if not packet.haslayer(Dot11):
		return
	if packet.type != 0 or packet.subtype != 0x04:
		return
	fields = []
	log_time = datetime.datetime.now().strftime("%H%M%S")
	fields.append(log_time)
	fields.append(packet.addr2)
	# rssi_val = -(256-ord(packet.notdecoded[-4:-3]))
	#fields.append(str(rssi_val))
	logger.info('\t'.join(fields))

def main():
	date = datetime.datetime.now().strftime("%m-%d-%Y:%H-%M-%S")
	logging.basicConfig(filename="output_%s.log" % date, level=logging.INFO, format='%(message)s')
	if(len(sys.argv) > 2):
                print("To many args. Only arg is -d for realtime output to stdout")
                sys.exit(1)
        elif(len(sys.argv) == 2):
		if(sys.argv[1] == '-d'):
			logger.addHandler(logging.StreamHandler(sys.stdout))
		else:
                	print("Only arg is -d for realtime output to stdout")
                	sys.exit(1)
	#logger.info(datetime.datetime.now().strftime("%m-%d-%Y"))
	sniff(iface=INTERFACE, prn=get_probes, store=0)

if __name__ == '__main__':
	main()
