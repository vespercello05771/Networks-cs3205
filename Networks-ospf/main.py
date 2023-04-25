import subprocess
import time
import argparse

ospf_command = "sudo /usr/sbin/ospfd -d"

routers = {
    'router1': '192.168.1.1',
    'router2': '192.168.1.2',
    'router3': '192.168.1.3'
}

parser = argparse.ArgumentParser(description='OSPF routing protocol')
parser.add_argument('-i', '--id', type=int, help='Node identifier value (i)', required=True)
parser.add_argument('-f', '--infile', type=str, help='Input file', required=True)
parser.add_argument('-o', '--outfile', type=str, help='Output file', required=True)
parser.add_argument('-b', '--hello', type=int, help='HELLO INTERVAL (in seconds)', required=True)
parser.add_argument('-a', '--lsa', type=int, help='LSA INTERVAL (in seconds)', required=True)
parser.add_argument('-s', '--spf', type=int, help='SPF INTERVAL (in seconds)', required=True)

args = parser.parse_args()

# Access the command-line arguments as follows
node_id = args.id
input_file = args.infile
output_file = args.outfile
hello_interval = args.hello
lsa_interval = args.lsa
spf_interval = args.spf

with open(input_file, 'r') as f:
# read the first line to get N and M
    line = f.readline().split()
    N, M = int(line[0]), int(line[1])

    # read the remaining lines to get the links
    links = []
    for i in range(M):
        line = f.readline().split()
        i, j, MinCij, MaxCij = int(line[0]), int(line[1]), int(line[2]), int(line[3])
        links.append((i, j, MinCij, MaxCij))
    
    
print(N,M,links)
print(node_id,hello_interval,lsa_interval,spf_interval)

for router, ip_address in routers.items():
    # Start the OSPF process as a subprocess
    process = subprocess.Popen(ospf_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Started OSPF process for {router} at {ip_address}.")
    time.sleep(1)