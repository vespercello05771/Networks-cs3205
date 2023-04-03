import socket
import os
import math
import sys
import time
import signal
import multiprocessing as mp


map_td= dict()
map_ad= dict()
ports = dict()
child_pids = []
def read_input_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = lines[1:-1] #since first and last lines are not required
    f.close()
    data = list()
    for line in lines:
        temp = list()
        if line[-1] == '\n':
            line = line[:-1]
        temp = line.split()
        data.append(temp)
    return data

def process_ads(K,ads_list, inputfilename):
    i= 0
    for ads in ads_list:
        with open(inputfilename) as f:
            lines = f.readlines()
        f.close()
        t = ads[0].strip()
        map_ad[t] = []
        for line in lines:
            if t in line:
                temp = line.rstrip('\n')
                map_ad[t].append(temp)
        
        ports[t] = K+55+i
        i = i+1
                    
                    
def write_data_to_root(K, data,inputfilename):
    TDS1 = data[2]
    TDS2 = data[3]
    ADS = [data[4],data[5],data[6],data[7],data[8],data[9]]
    
    

    td1 = TDS1[0].split('_')[1].strip()
    td2 = TDS2[0].split('_')[1].strip()
    map_td[td1] = []
    map_td[td2] = []
    ports['root'] = K+53
    ports[td1] = K+54
    ports[td2] = K+55
    for i in range(4,10):
        if data[i][0].split('.')[1] == td1:
           
            map_td[td1].append(data[i])
        else:
            map_td[td2].append(data[i])

    process_ads(K,ADS,inputfilename)
    
    
def start_server(command, childpids):
    pid = os.fork()
    if pid == 0:
        os.system(command)
        sys.exit(0)
    else:
        childpids.append(pid)
                    
       
def write_dic(dict,filename):
    fp = open(filename,'a+')
    for key in dict :
        fp.write(f'{key} {dict[key]}\n')
    fp.close()
                 
def main():
    n = len(sys.argv)
    childpids = []
    if n != 3:
        print("INPUT SEQUENCE IS WRONG PLEASE CORRECT IT")
    else:
        K = int(sys.argv[1])
        inputfilename = str(sys.argv[2]).strip()

        data = read_input_file(inputfilename)
      
        pnos = {}
    
        write_data_to_root(K,data, inputfilename)
        
        #opening name resolver server
        start_server("python3 NR.py " + data[0][1].strip()+' '+str(K+53), childpids)

        # opening all servers
        servers = data[1:10]
        val = 1
        for i in servers:
            msg =  i[1].strip()+ ' ' + str(K + 53 + val)
            if i[0].strip()[0:3] == "RDS" :
                command="python3 RDS.py"
            elif i[0].strip()[0:3] == "TDS" :
                command="python3 TDS.py"
            else :
                command="python3 ADS.py"
            
            start_server(command + ' ' + msg+ ' ', childpids)
            val +=1
            time.sleep(1)
            
        
        write_dic(ports,"ports.txt")
        fp = open("root.txt","a+")
        fp.write(f"{data[2][0][4:]} {data[2][1]}\n")
        fp.write(f"{data[3][0][4:]} {data[3][1]}\n")
        fp.close()
        write_dic(map_ad,"ads.txt")
        write_dic(map_td,"tds.txt")
        while True:
            domain_name = input("Enter Server Name: ")
            if domain_name == "bye":
                for child_pid in child_pids:
                    os.kill(child_pid, signal.SIGSTOP)
                print("All Server Processes are killed. Exiting.")
                break
            else:
                domain_name = f"{domain_name} {data[1][1].strip()} {str(K)}"
                client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                client_socket.sendto(domain_name.strip().encode(), (data[0][1].strip(), K + 53))
                data, addr = client_socket.recvfrom(1024)
                print("Received:", data.decode())
    
if __name__ == '__main__':
    main()