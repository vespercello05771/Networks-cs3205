import socket

server_address = ('localhost', 10000)
window_size = 5

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(server_address)

expected_sequence_number = 0
received_packets = []

while expected_sequence_number < 100:
    data, address = socket.recvfrom(1024)
    packet_sequence_number = int(data.decode())
    if packet_sequence_number == expected_sequence_number:
        received_packets.append(packet_sequence_number)
        expected_sequence_number += 1
        if expected_sequence_number % window_size == 0:
            for i in range(expected_sequence_number - window_size, expected_sequence_number):
                packet = str(i).encode()
                socket.sendto(packet, address)
    else:
        packet = str(expected_sequence_number - 1).encode()
        socket.sendto(packet, address)

socket.close()
