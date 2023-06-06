# Name: Youssef Mohamed Anwar

import os
import sys
import re
import time
import socket
import numpy as np
from scapy.all import *

try:
    path = sys.argv[1]
except:
    print ("ERROR: need path to pcap file")
    sys.exit(0)

packets = rdpcap(path)

count = 0
totalpackets = 0
totalbytes = 0
Source_ports = []
Destination_ports = []
modes = []

print (                                       )
print ("-------------------------------------")
print ("Gathering infromation form ", path, "...................")
print ("-------------------------------------")
time.sleep(2)

for pkt in packets: 

	#finds the total packets 
	totalpackets+=1
	
	
	try:
		#find all the packets for port 21
		if (pkt.dport == 21 or pkt.sport == 21) and pkt.haslayer(Raw):
			count+=1
				
		#find username and password
		if pkt.load.find(b'USER') >= 0:
			print ("Username obtained: " , pkt.load.decode('UTF-8'))
			
		if pkt.load.find(b'PASS') >= 0:
			print ("Password obtained: " , pkt.load.decode('UTF-8'), "\n-------------------------")
			
			
		#find desitnation and source ports
		if pkt.load.find(b'ftp-data'):
			Source_ports.append(pkt.sport)
			Destination_ports.append(pkt.dport)
			
			#gets the total number of bytes 
			totalbytes += pkt.len
	
		#find FTP modes
		if pkt.load.find(b'mode') >= 0 or pkt.load.find(b'Mode') >= 0:
			modes.append(pkt.load.decode('UTF-8'))

			
		
			
		
	except (Exception) as e:
		pass

print ("")
print (">>> The number of port 21 packets is ", count)

print (">>> The nubmer of bytes transfered in the ftp data transfer is ", totalbytes) 

print (">>> The following modes of FTP connections were found:") 

for a in modes:
	print (a)
print (">>> Source ports used for ftp data are: ",set(Source_ports))

print (">>> Destination ports used for ftp data are: ",set(Destination_ports))

print (">>> The number of non-ftp packets is ", totalpackets-count)



