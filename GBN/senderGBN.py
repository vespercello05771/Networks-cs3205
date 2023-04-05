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
import time
import argparse
import sys
import datetime
import threading

PACKET_LENGTH = 1024
PACKET_GEN_RATE = 1  # packets per second
MAX_PACKETS = 1000
WINDOW_SIZE = 20
MAX_BUFFER_SIZE = 30
DEBUG  = 0
server = 'localhost'
port = 5000
TIMEOUT = 100
Retransmission_attempts = []
RTT = []
#getting the list of command line options
argumentList = sys.argv[1:]

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="enable debugging mode", action="store_true")
parser.add_argument("-s", "--server", help="server IP address")
parser.add_argument("-p", "--port", help="server port number", type=int)
parser.add_argument("-l", "--pl", help="Packet Length", type = int)
parser.add_argument("-r", "--pgr", help="packet generation rate", type = int)
parser.add_argument("-n", "--mp", help="maximum packets", type=int)
parser.add_argument("-w", "--ws", help="window size", type = int)
parser.add_argument("-f", "--mbs", help="max buffer size", type = int)

args = parser.parse_args()

if args.debug:
    DEBUG = 1
    print("Debug mode is enabled")
if args.server:
    sever = args.server
    print("Reciever is : ", args.server)
if args.port:
    port = args.port
    print("Receiver port number is", args.port)
if args.pl:
    PACKET_LENGTH = args.packet_length
if args.pgr:
    PACKET_GEN_RATE = args.pgr
if args.mp:
    MAX_PACKETS = args.mp
if args.ws:
    WINDOW_SIZE = args.ws
if args.mbs:
    MAX_BUFFER_SIZE = args.mbs
    
BUFFER_SIZE = 0
# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the server address and port
server_address = (server, port)

sequence_number = 0
    
# Send packets continuously
while True:
    
    if BUFFER_SIZE == MAX_BUFFER_SIZE :
      continue 
      
    # send packet
    packet_data = b'0' * PACKET_LENGTH
    
    packet_data = packet_data + str(sequence_number).encode()
   
    current_time = datetime.datetime.now()

    # Format the time with milliseconds and microseconds
    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    client_socket.sendto(packet_data, server_address)
    BUFFER_SIZE +=1 
    
    #RECIEVE THE ACK DATA      
    ack_data  = client_socket.recvfrom(BUFFER_SIZE)
    time_str_ack = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    RTT.append(time_str_ack - time_str)
    if(RTT.size() == 10) :
        TIMEOUT = sum(RTT)/RTT.length
    # Print packet information
    print(f"PACKET GENERATION RATE : {PACKET_GEN_RATE}\nPACKET_LENGTH : {PACKET_LENGTH}\nRetransmission ratio : {1}\nAverage RTT value for all Acknowledged Packets : {2}")
    
    if(DEBUG == 1) :
        print(f"Seq #: {sequence_number}  \nTime Generated : {time_str}\nRTT : {RTT}\n Number of Attempts : {NOA} ")
    # Wait for the next packet generation
    time.sleep(1 / PACKET_GEN_RATE)
    
    # Increment sequence number
    sequence_number += 1



socket.close()