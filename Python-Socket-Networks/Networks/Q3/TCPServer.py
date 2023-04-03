#https://pythontic.com/modules/socket/send
import socket 
from pathlib import Path

serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('',serverPort))

serverSocket.listen(1)

print("The server is ready to receive")

while (True):
    (connectionSocket, clientAddress) = serverSocket.accept()
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
    clientMsg = connectionSocket.recv(1024).decode()
    filename,filesize = clientMsg.split()
    
    try :
        f = open(f"{filename}.txt","rb")
        f.seek(-int(filesize),2)
        txt = f.read()
        try : 
            f2 = open(f"{filename}1.txt","ab")
            f2.write(txt)  
            connectionSocket.send(f"appended last {str(filesize)} bytes to {filename}1.txt".encode())  
            break
        except :
            connectionSocket.send(f"Server says that the file {filename}1.txt does not exist".encode())
            break
    except :
        connectionSocket.send("SORRY!".encode())
        break
    
    connectionSocket.close()
