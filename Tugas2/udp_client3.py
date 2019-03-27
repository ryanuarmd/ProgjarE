import socket
import select

UDP_IP = "127.0.0.3"
IN_PORT = 9000
timeout = 5


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    data1 = data[:7] + "new3.png" 
    print(data1)
    if data1:
        print "File:", data1
        file_name = data1

    f = open(file_name, 'wb')

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data1, addr = sock.recvfrom(9216)
            f.write(data1)
        else:
            print "%s Finish!" % file_name
            f.close()
            break
