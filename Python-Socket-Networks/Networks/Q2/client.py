#https://pythontic.com/modules/socket/udp-client-server-example
import socket
import sys

serverAddressPort   = ("127.0.0.2", 20001) #contains server ip and server port
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
     

while(True):
    msgFromClient = input("enter command : ")
    if(msgFromClient == "endproc"):
        print("EndOfProcess")
        UDPClientSocket.sendto(msgFromClient.encode(),serverAddressPort)
        break
    
    bytesToSend = msgFromClient.encode()
    #Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server: {}".format(msgFromServer[0].decode())
    print(msg)
    
UDPClientSocket.close()




