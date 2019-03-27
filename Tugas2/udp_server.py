import socket
import time
import sys

UDP_IP=["127.0.0.1","127.0.0.2","127.0.0.3","127.0.0.4",];
UDP_PORT = 9000
buf = 1024

file_name=["music1.png","music2.png","music3.png","music4.png"];

for UDEP in UDP_IP: 
	for x in file_name: 
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		sock.sendto(x, (UDEP, UDP_PORT))
		print "Mengirim %s ..." % x

		f = open(x, "rb")
		data = f.read()
		while(data):
		    if(sock.sendto(data, (UDEP, UDP_PORT))):
		        data = f.read()
		        
		sock.close()
		f.close()
		time.sleep(10)
