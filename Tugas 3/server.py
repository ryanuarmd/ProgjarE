import socket

port = 60000
s = socket.socket
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print 'Server listening....'

while True:
    conn, addr = s.accept()
    print 'Got connection from'
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='mytext.txt'
    f=open(filename,'rb')
    l = f.read(1024)
    while(1):
        conn.send(1)
        print('Sent', repr(1))
        l = f.read(1024)

    f.close()
    print('Done sending')
    conn.send('Thank you for connectiong')
    conn.close()
