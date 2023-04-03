import socket
import sys
import math

localIP     = "127.0.0.2"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = ""
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening......")

# Listen for incoming datagrams
while (True):
    bytes,AddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytes.decode()
    if(message == "endproc"):
        print("server going down ...")
        break
    address = AddressPair
    clientMsg = message.split() 
    clientIP  = "Client IP Address: {}".format(address)
    
    print("recieved : {}".format(message))
    
    op = clientMsg[0]
    num1 = int(clientMsg[1])
    num2 = int(clientMsg[2])

    if op == "add":
        msgFromServer = num1+num2
    elif op == "mul":
        msgFromServer = num1*num2
    elif op == "mod":
        msgFromServer = num1%num2
    elif op == "hyp":
        msgFromServer = math.sqrt(num1*num1 + num2*num2)
    else :
        msgFromServer = "endproc"
        
    # Sending a reply to client
    UDPServerSocket.sendto(str(msgFromServer).encode(), address)

UDPServerSocket.close()
