import socket
import sys
import os

serversocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
serversocket.bind((str(sys.argv[1]),int(sys.argv[2])))
while True:
    data,addr = serversocket.recvfrom(2048)
    data = data.decode().strip()
    filename = 'root.txt'
    check = 0
    with open(filename,'r') as f:
        lines = f.readlines()

    found=''
    for line in lines:
        if(line[-1]=='\n'):
            line = line[:-1]
        temp = line.split()[0]
        if(temp.split('_')[1]==data):
            check = 1
            found = line
            msg = line.split()[1].strip()
    if check==0:
        msg ="ERROR 404"

    o = open('rootOutput.txt','a+')
    o.write("recieved request : "+str(data))
    o.write('\n')
    o.write("found : "+str(found))
    o.write('\n')
    o.write("sending : "+msg)
    o.write('\n')
    o.write('****************************************')
    o.write('\n')
    o.close()
    serversocket.sendto(msg.encode(),addr)




