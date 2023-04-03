#https://pythontic.com/modules/socket/send
import socket
serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

filename = input("enter filename : ")
filesize = input("enter filesize : ")
clientSocket.send((filename + " " +str(filesize)).encode())

msgFromServer = clientSocket.recv(1024)
print(msgFromServer.decode())
clientSocket.close()
