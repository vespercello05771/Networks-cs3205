import socket
import sys
import os

n = len(sys.argv)
if(n!=3):
    nro = open("NR_OUTPUT.txt",'a+')
    nro.write("INPUT SEQUENCE IS WRONG")
    nro.write('\n')
    nro.write("*************************")
    nro.write('\n')
    nro.close()
else:
    nro = open("NR_OUTPUT.txt",'a+')
    pnos = open('portNumbers.txt','r')
    numbers = pnos.readlines()
    pnos.close()
    # print("hey")   
    serversocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    serversocket.bind((str(sys.argv[1]),int(sys.argv[2])))
    while True:
        data,client_addr = serversocket.recvfrom(2048)
        data = data.decode().split()
        roothost = data[1]
        Port = int(data[-1])
        domainName = data[0]
        # split domain name
        togetTDS = domainName.split('.')[-1]
        togetADS = domainName.split('.')[-2]
        # calling root
        rootportno= ''
        for num in numbers:
            if 'root' in num and len(num.split())==2 :
                rootportno=int(num.split()[-1])
        # print(rootportno) 
        nro.write("sending request to root.. Request name : "+togetTDS) 
        nro.write("\n")      
        rootclient = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        rootclient.sendto(togetTDS.encode(),(roothost,Port+rootportno))
        rootdata,rootaddr = rootclient.recvfrom(2048)
        if(rootdata.decode().strip()=="ERROR 404"):
            serversocket.sendto(rootdata,client_addr) 
            nro.write("Recieved msg from root : "+rootdata.decode())  
            nro.write('\n')
            nro.write("*************************")
            nro.write('\n')
            nro.close()
        else:
            # calling tldserver
              
            tldhost = rootdata.decode()
            tldclient = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
            tldportno = ''
            tempo = domainName.split('.')[-1]
            for num in numbers:
                if 'TDS' in num and tempo in num and len(num.split())==3:
                    tldportno=int(num.split()[-1])
            # print(tldportno)
            nro.write("sending request to TLD server.. Request name : "+domainName) 
            nro.write("\n") 
            tldclient.sendto(domainName.encode(),(tldhost,Port+tldportno))
            tldData,Tldaddr = tldclient.recvfrom(2048)
            if(tldData.decode().strip()=="ERROR 404"):
                serversocket.sendto(tldData,client_addr) 
                nro.write("Recieved msg from root : "+rootdata.decode())  
                nro.write('\n')
                nro.write("*************************")
                nro.write('\n')
                nro.close()  
            else:
                # calling ads server
                domainclient = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
                adminportno = ''
                tempo = domainName.split('.')[-2]
                for num in numbers:
                    if 'ADS' in num and tempo in num and len(num.split())==3:
                        adminportno=int(num.split()[-1])
                # print(adminportno)
                adminhost = tldData.decode()
                domainclient.sendto(domainName.encode(),(adminhost,Port+adminportno))
                finaldata,addr = domainclient.recvfrom(2048)
                serversocket.sendto(finaldata,client_addr)
                




