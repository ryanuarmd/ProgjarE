import socket
server_socket = socket.socket()
server_name = 'localhost'
server_port = 12345
server_socket.bind((server_name, server_port))
server_socket.listen(5)

while True:
    c, address = server_socket.accept()
    print "We got connection from", address
    c.send("Connected to Server!")
    c.close()
    
