import socket
import sys
import os

serversocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
serversocket.bind((str(sys.argv[1]),int(sys.argv[2])))
while True:
    data,addr = serversocket.recvfrom(2048)
    domain = data.decode().split('.')
    filename = domain[1]+'.'+domain[2]+'.'+'txt'
    with open(filename,'r') as f:
        lines = f.readlines()
    check=0
    for line in lines:
        if(line[-1]=='\n'):
            line = line[:-1]
        temp = line.split()
        if(temp[0]==data.decode().strip()):
            check=1
            msg = temp[1]

    if check==0:
        msg ="ERROR 404"
    o = open('AuthOutput.txt','a+')
    o.write("recieved request : "+str(data.decode()))
    o.write('\n')
    o.write("sending : "+msg)
    o.write('\n')
    o.write('****************************************')
    o.write('\n')
    o.close()
    serversocket.sendto(msg.encode(),addr) 