#https://pythontic.com/modules/socket/udp-client-server-example
import socket
import sys


msgFromClient       = sys.argv[1]
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001) #contains server ip and server port
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

#Wait on recvfrom()
msgFromServer = UDPClientSocket.recvfrom(bufferSize)

#Wait completed
msg = "Message from Server: {}".format(msgFromServer[0].decode())

print(msg)
