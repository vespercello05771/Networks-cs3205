import socket
import sys

def read_port_numbers(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    if len(sys.argv) != 3:
        with open('NR_OUTPUT.txt', 'a+') as f:
            f.write("INPUT SEQUENCE IS WRONG\n")
            f.write("*************************\n")
        return

    with open('NR_OUTPUT.txt', 'a+') as nro:
        numbers = read_port_numbers('ports.txt')
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serversocket.bind((str(sys.argv[1]), int(sys.argv[2])))

        while True:
            data, client_addr = serversocket.recvfrom(2048)
            domain_parts = data.decode().split('.')
            togetTDS = domain_parts[-1]
            togetADS = domain_parts[-2]
            roothost, Port = domain_parts[1], int(domain_parts[-1])

            # calling root
            rootportno = next(int(num.split()[-1]) for num in numbers
                              if 'root' in num and len(num.split()) == 2)
            nro.write(f"sending request to root.. Request name : {togetTDS}\n")
            rootclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            rootclient.sendto(togetTDS.encode(), (roothost, Port + rootportno))
            rootdata, rootaddr = rootclient.recvfrom(2048)

            if rootdata.decode().strip() == "ERROR 404":
                serversocket.sendto(rootdata, client_addr)
                nro.write(f"Recieved msg from root : {rootdata.decode()}\n")
                nro.write("*************************\n")
                continue

            # calling tldserver
            tldhost = rootdata.decode()
            tldportno = next(int(num.split()[-1]) for num in numbers
                              if 'TDS' in num and togetTDS in num and len(num.split()) == 3)
            nro.write(f"sending request to TLD server.. Request name : {'.'.join(domain_parts)}\n")
            tldclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tldclient.sendto('.'.join(domain_parts).encode(), (tldhost, Port + tldportno))
            tldData, Tldaddr = tldclient.recvfrom(2048)

            if tldData.decode().strip() == "ERROR 404":
                serversocket.sendto(tldData, client_addr)
                nro.write(f"Recieved msg from root : {rootdata.decode()}\n")
                nro.write("*************************\n")
                continue

            # calling ads server
            adminhost = tldData.decode()
            adminportno = next(int(num.split()[-1]) for num in numbers
                                if 'ADS' in num and togetADS in num and len(num.split()) == 3)
            domainclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            domainclient.sendto('.'.join(domain_parts).encode(), (adminhost, Port + adminportno))
            finaldata, addr = domainclient.recvfrom(2048)
            serversocket.sendto(finaldata, client_addr)

if __name__ == '__main__':
    main()
