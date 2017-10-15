import socket
import sys
from thread import *

host = '127.0.0.1'
port = 5252

mainSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mainSock.bind((host,port))
except socket.error as e:
    print(str(e))

print("Socket Address .:")
print(mainSock)
server_ip = socket.gethostbyname(host)
print("Servers IP address .: \n" + server_ip)
mainSock.listen(2)
print('Waiting for a connection .:... ')


connec1, addr = mainSock.accept()
connec2, addr2 = mainSock.accept()
print('Connected to.:...(ip)' + addr[0] + '::(port)' + str(addr[1]))
print('Connected to.:...(ip)' + addr2[0] + '::(port)' + str(addr2[1]))
#mainSock.settimeout(10)

message = 'Hello from server'
connec1.send(message.encode())
connec2.send(message.encode())

data = connec1.recv(1024).decode()
data2 = connec2.recv(1024).decode()

print('Recieved from client (1) .: ' + data)

print('Recieved from client (2) .: ' + data2)