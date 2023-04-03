#https://pythontic.com/modules/socket/udp-client-server-example
import socket

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = ""
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")
    
# Listen for incoming datagrams
while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode()
    address = bytesAddressPair[1]
    clientMsg = message
    clientIP  = "Client IP Address: {}".format(address)
    print("msg from client :\n{}".format(clientMsg))
    print(clientIP)
    msgFromServer = clientMsg
    # Sending a reply to client
    UDPServerSocket.sendto(msgFromServer.encode(), address)

UDPServerSocket.close()