import socket
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])

def handle_request(data, addr):
    data = data.decode().strip()
    filename = 'root.txt'

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        found = ''
        msg = "ERROR 404"
        for line in lines:
            line = line.rstrip('\n')
            temp = line.split()
            if temp[0].split('_')[1] == data:
                found = line
                msg = temp[1]
                break

        with open('rootOutput.txt', 'a+') as f:
            f.write(f"received request: {data}\n")
            f.write(f"found: {found}\n")
            f.write(f"sending: {msg}\n")
            f.write("****************************************\n")

        serversocket.sendto(msg.encode(), addr)

    except FileNotFoundError:
        pass

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.bind((HOST, PORT))

while True:
    data, addr = serversocket.recvfrom(2048)
    handle_request(data, addr)
