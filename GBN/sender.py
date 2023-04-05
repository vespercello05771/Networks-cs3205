import socket
import time
import threading

server_address = ('localhost', 10000)
window_size = 5
timeout = 0.1

sequence_number = 0
sent_packets = []
acknowledged_packets = []

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.settimeout(timeout)

def send_packet(packet):
    socket.sendto(packet, server_address)
    sent_packets.append(packet)

def receive_acknowledgements():
    while True:
        try:
            data, address = socket.recvfrom(1024)
            packet_sequence_number = int(data.decode())
            acknowledged_packets.append(packet_sequence_number)
        except socket.timeout:
            pass

def start_sender():
    threading.Thread(target=receive_acknowledgements, daemon=True).start()
    sequence_number =0
    while sequence_number < 100:
        if sequence_number < len(sent_packets) - window_size:
            continue
        packet = str(sequence_number).encode()
        send_packet(packet)
        sequence_number += 1
        if sequence_number == 10:
            start_time = time.time()
        if sequence_number > 10:
            estimated_rtt = time.time() - start_time
            timeout = 2 * estimated_rtt
            socket.settimeout(timeout)
        time.sleep(0.01)

    socket.close()

if __name__ == '__main__':
    start_sender()
