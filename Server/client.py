## Ryan Le Bon 
## October 15, 2017
## Github @Ryanbbq
import socket


host = '127.0.0.1'
port = 5252

mainSock = socket.socket()
mainSock.connect((host,port))

message = 'Hello from client (Alice)'
mainSock.send(message.encode())

data = mainSock.recv(1024).decode()

print('Received from server : ' + data)


mainSock.close()
## Ryan Le Bon 
## October 15, 2017
## Github @Ryanbbq