from threading import Thread
import socket
import os

TARGET_IP = "127.0.0.1"
TARGET_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((TARGET_IP, TARGET_PORT))

namafile=["music1.png","music2.png","music3.png","music4.png"];

def sendImage(CLIENT_IP, CLIENT_PORT):
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
 
      f.close() 

while True:
   print "Loading..."
   data, addr = sock.recvfrom(1024)
   if(data=="READY"):
      thread = Thread(target=sendImage, args=(addr))
      thread.start()
