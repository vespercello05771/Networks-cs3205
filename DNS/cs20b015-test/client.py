import socket
import os,signal
import math
# import regex as re
import sys
import time
import multiprocessing as mp
#reading arguments

n = len(sys.argv)
childpids = []
if(n!=3):
    print("INPUT SEQUENCE IS WRONG PLEASE CORRECT IT")

else:
    k = int(sys.argv[1])
    inputfilename = str(sys.argv[2]).strip()

    pnos = open('portNumbers.txt','w')

    # reading lines from input file
    try:
        with open(inputfilename) as f:
            lines = f.readlines()
        lines = lines[1:-1]
        f.close()
        scrapLines = []
        for line in lines:
            temp = []
            if(line[-1]=='\n'):

                line = line[:-1]
            temp = line.split()
            scrapLines.append(temp)
        # print(scrapLines)
        NR_server = scrapLines[0]
        RDS_server = scrapLines[1]
        TDS1 = scrapLines[2]
        TDS2 = scrapLines[3]

        # writing data into root
        r = open('root.txt','w')
        pnos.write('root 54')
        pnos.write('\n')
        r.write(scrapLines[2][0]+' '+scrapLines[2][1])
        r.write('\n')
        r.write(scrapLines[3][0]+' '+scrapLines[3][1])
        r.close()
        one = scrapLines[2][0].split('_')[1].strip()
        pnos.write('TDS '+scrapLines[2][0].split('_')[1].strip()+' '+'55')
        pnos.write('\n')
        two = scrapLines[3][0].split('_')[1].strip()
        pnos.write('TDS '+scrapLines[3][0].split('_')[1].strip()+' '+'56')
        pnos.write('\n')
        #writing ADS for servers
        ADS1 = scrapLines[4]
        pnos.write('ADS '+scrapLines[4][0].strip()+' '+'57')
        pnos.write('\n')
        ADS2 = scrapLines[5]
        pnos.write('ADS '+scrapLines[5][0].strip()+' '+'58')
        pnos.write('\n')
        ADS3 = scrapLines[6]
        pnos.write('ADS '+scrapLines[6][0].strip()+' '+'59')
        pnos.write('\n')
        ADS4 = scrapLines[7]
        pnos.write('ADS '+scrapLines[7][0].strip()+' '+'60')
        pnos.write('\n')
        ADS5 = scrapLines[8]
        pnos.write('ADS '+scrapLines[8][0].strip()+' '+'61')
        pnos.write('\n')
        ADS6 = scrapLines[9]
        print(ADS1)
        pnos.write('ADS '+scrapLines[9][0].strip()+' '+'62')
        pnos.write('\n')
        pnos.close()
        onefilename = str(one)+'.'+'txt'
        twofilename = str(two)+'.'+'txt'
        o = open(onefilename,'w')
        t = open(twofilename,'w')
        for i in range(4,10):
            if scrapLines[i][0].split('.')[1]==one:
                o.write(scrapLines[i][0]+' '+scrapLines[i][1])
                o.write('\n')
            else:
                t.write(scrapLines[i][0]+' '+scrapLines[i][1])
                t.write('\n')
        o.close()
        t.close()

        # creating data bases for ADS's info



        # for ads1
            filename = ADS1[0]+'.'+'txt'
            with open(inputfilename) as fl:
                lines = fl.readlines()
            fl.close()
            ads1 = open(filename,'w')
            t = ADS1[0].strip()
            for line in lines:
                if t in line:
                    temp = ''
                    if(line[-1]=='\n'):
                        temp = line[:-1]
                    else:
                        temp = line
                    ads1.write(temp)
                    ads1.write('\n')
            ads1.close()
                
            #for ads2
            
            filename = ADS2[0]+'.'+'txt'
            with open(inputfilename) as fl:
                lines = fl.readlines()
            fl.close()
            ads2 = open(filename,'w')
            t = ADS2[0].strip()
            for line in lines:
                if t in line:
                    temp = ''
                    if(line[-1]=='\n'):
                        temp = line[:-1]
                    else:
                        temp = line
                    ads2.write(temp)
                    ads2.write('\n')
            ads2.close()

            #for ads3
            filename = ADS3[0]+'.'+'txt'
            with open(inputfilename) as fl:
                lines = fl.readlines()
            fl.close()
            ads3 = open(filename,'w')
            t = ADS3[0].strip()
            for line in lines:
                if t in line:
                    temp = ''
                    if(line[-1]=='\n'):
                        temp = line[:-1]
                    else:
                        temp = line
                    ads3.write(temp)
                    ads3.write('\n')
            ads3.close()

            #for ads4
            filename = ADS4[0]+'.'+'txt'
            with open(inputfilename) as fl:
                lines = fl.readlines()
            fl.close()
            ads4 = open(filename,'w')
            t = ADS4[0].strip()
            for line in lines:
                if t in line:
                    temp = ''
                    if(line[-1]=='\n'):
                        temp = line[:-1]
                    else:
                        temp = line
                    ads4.write(temp)
                    ads4.write('\n')
            ads4.close()

            #for ads5
            filename = ADS5[0]+'.'+'txt'
            with open(inputfilename) as fl:
                lines = fl.readlines()
            fl.close()
            ads5 = open(filename,'w')
            t = ADS5[0].strip()
            for line in lines:
                if t in line:
                    temp = ''
                    if(line[-1]=='\n'):
                        temp = line[:-1]
                    else:
                        temp = line
                    ads5.write(temp)
                    ads5.write('\n')
            ads5.close()

            #for ads6
            filename = ADS6[0]+'.'+'txt'
            with open(inputfilename) as fl:
                lines = fl.readlines()
            fl.close()
            ads6 = open(filename,'w')
            t = ADS6[0].strip()
            for line in lines:
                if t in line:
                    temp = ''
                    if(line[-1]=='\n'):
                        temp = line[:-1]
                    else:
                        temp = line
                    ads6.write(temp)
                    ads6.write('\n')
            ads6.close()
        # print(k)

        # opening name resolver server
        pid = os.fork()
        if(pid==0):
            nrhostname = NR_server[1].strip()
            portNo = k+53
            os.system("python3 NRServer.py "+nrhostname+' '+str(portNo))
            sys.exit(0)
        else:
            childpids.append(pid)
        time.sleep(1)
        # opening all servers
        pid = os.fork()
        if(pid==0):
            msg = RDS_server[1].strip()+' '+str(k+54)
            os.system('python3 RootServer.py '+msg)
            sys.exit(0)
        else:
            childpids.append(pid)
        pid = os.fork()
        
        if(pid==0):
            msg = TDS1[1].strip()+' '+str(k+55)
            os.system('python3 TLDserver.py '+msg)
            sys.exit(0)
        else:
            childpids.append(pid)
        pid = os.fork()
        if(pid==0):
            msg = TDS2[1].strip()+' '+str(k+56)
            os.system('python3 TLDserver.py '+msg)
            sys.exit(0)
        else:
            childpids.append(pid)
        pid = os.fork()
        if(pid==0):
            msg = ADS1[1].strip()+' '+str(k+57)
            os.system('python3 Aservers.py '+msg)
            sys.exit(0)
        else:
            childpids.append(pid)
        pid = os.fork()
        if(pid==0):
            msg = ADS2[1].strip()+' '+str(k+58)
            os.system('python3 Aservers.py '+msg)
            sys.exit(0)
        else:
            childpids.append(pid)
        pid = os.fork()
        if(pid==0):
            msg = ADS3[1].strip()+' '+str(k+59)
            os.system('python3 Aservers.py '+msg)
            sys.exit(0)
        else:
            childpids.append(pid)
        pid = os.fork()
        if(pid==0):
            msg = ADS4[1].strip()+' '+str(k+60)
            os.system('python3 Aservers.py '+msg)
            sys.exit(0)
        else:
            childpids.append(pid)
        pid = os.fork()
        if(pid==0):
            msg = ADS5[1].strip()+' '+str(k+61)
            os.system('python3 Aservers.py '+msg)
            sys.exit(0)
        else:
            childpids.append(pid)
        pid = os.fork()
        if(pid==0):
            msg = ADS6[1].strip()+' '+str(k+62)
            os.system('python3 Aservers.py '+msg)
            sys.exit(0)
        else:
            childpids.append(pid)
        time.sleep(1)
        while(True):
            clientSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
            domainName = input("Enter Server Name: ")
            if(domainName=="bye"):
                for child in childpids:
                    os.kill(child,signal.SIGSTOP)
                print("All Server Processes are killed. Exiting.")
                break
            else:
                domainName = domainName+' '+ RDS_server[1].strip() + ' '+str(k)
                # print("Searching......")
                clientSocket.sendto(domainName.strip().encode(), (NR_server[1].strip(),k+53))
                data, addr = clientSocket.recvfrom(1024)
                print('Received:', data.decode())
                # clientSocket.close()
    except FileNotFoundError as e:
        print(" Please give the correct file name!")

    #  making a list of lists to scrape data from input.txt to make mini databases for servers
    







# print(scrapLines)