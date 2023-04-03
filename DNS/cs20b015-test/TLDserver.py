import socket
import sys
import os

serversocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
serversocket.bind((str(sys.argv[1]),int(sys.argv[2])))
while True:
    data,addr = serversocket.recvfrom(2048)
    data = data.decode()
    tld = data.split('.')[-1]
    filename = tld+'.'+'txt'
    mainname = data.split('.')[-2]
    with open(filename,'r') as f:
        lines = f.readlines()
    check=0
    found = ''
    for line in lines:
        if(line[-1]=='\n'):
            line = line[:-1]
        temp = line.split()
        if(temp[0].split('.')[0]==mainname):
            found = line
            check=1
            msg = temp[1]
    if check==0:
        msg ="ERROR 404"
    o = open('TLDOutput.txt','a+')
    o.write("recieved request : "+str(data))
    o.write('\n')
    o.write("found : "+str(found))
    o.write('\n')
    o.write("Sending : "+msg)
    o.write('\n')
    o.write('****************************************')
    o.write('\n')
    o.close()
    serversocket.sendto(msg.encode(),addr)