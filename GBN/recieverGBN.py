"""
 NAME: Satya Venkata Sai Teja P
 Roll Number: CS20B072
 Course: CS3205 Jan. 2023 semester
 Lab number: 4
 Date of submission: <fill>
 I confirm that the source file is entirely written by me without
 resorting to any dishonest means.
 Website(s) that I used for basic socket programming code are:
 URL(s): https://www.geeksforgeeks.org/udp-server-client-implementation-c/
 Client side implementation of UDP client-server model

"""

import socket
import random
import sys
import argparse

PACKET_LENGTH = 1024
NFE = 0
MAX_PACKETS = 0
PER = 0.5
server_port = 5000
DEBUG = 0
BUFFER_LENGTH = 0
#getting the list of command line options
argumentList = sys.argv[1:]

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="enable debugging mode", action="store_true")
parser.add_argument("-p", "--port", help="reviever port number",type = int)
parser.add_argument("-n", "--mp", help="MAX PACKETS", type=int)
parser.add_argument("-e", "--per", help="Packet Error Rate", type=float)

args = parser.parse_args()

if args.debug:
    DEBUG = 1
if args.port:
    server_port = args.port
if args.mp:
    MAX_PACKETS = args.mp
if args.per:
    PER = args.per

    
# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the server address and port
server_address = ('localhost', server_port)
server_socket.bind(server_address)

# Receive packets continuously
while True:
    #init ack
    ack_data = "0".encode()
    
    # Receive a packet
    packet_data, client_address = server_socket.recvfrom(1024)
    
    # Extract sequence number from the packet
    sequence_number = int(packet_data[-8:].decode())
    
    # Randomly drop the packet
    if random.random() < PER:
        # Print dropped packet information
        print(f"Dropped packet {sequence_number}")
        continue
    
    if BUFFER_LENGTH == MAX_PACKETS : 
        print("Max buffer length reached!")
        continue
    
    # Print received packet information
    print(f"Received packet {sequence_number}")
    BUFFER_LENGTH = 0
    
    #check NFE
    if NFE == sequence_number :
        NFE+=1
        #send ack
        ack_data = str(sequence_number).encode()
        server_socket.sendto(ack_data,client_address)
    else :
        #send cumulative ack
        server_socket.sendto(ack_data,client_address)
    

socket.close()
