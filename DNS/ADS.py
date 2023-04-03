import socket
import sys
import os

def get_filename(data):
    domain = data.decode().split('.')
    return domain[1] + '.' + domain[2] + '.' + 'txt'

def search_file(data, filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line[-1] == '\n':
            line = line[:-1]
        temp = line.split()
        if temp[0] == data.decode().strip():
            return temp[1]
    return "ERROR 404"

def log_request(data, msg):
    with open('AuthOutput.txt', 'a+') as o:
        o.write("received request: " + str(data.decode()) + '\n')
        o.write("sending: " + msg + '\n')
        o.write('****************************************\n')

def start_server(ip, port):
    serversocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    serversocket.bind((ip, port))
    while True:
        data, addr = serversocket.recvfrom(2048)
        filename = get_filename(data)
        msg = search_file(data, filename)
        log_request(data, msg)
        serversocket.sendto(msg.encode(), addr)

if __name__ == '__main__':
    start_server(sys.argv[1], int(sys.argv[2]))
