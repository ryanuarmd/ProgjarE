import socket
client_socket = socket.socket()
server_address = 'localhost'
server_port = 12345
client_socket.connect((server_address, server_port))
data = client_socket.recv(1024)
print data

client_socket.close()
input('Enter to Exit')
