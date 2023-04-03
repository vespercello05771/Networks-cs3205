import socket

# Define constants
ROOT_SERVER_ADDRESS = ('localhost', 12000)
TLD_SERVER_ADDRESS = {
    '.com': ('localhost', 12001),
    '.edu': ('localhost', 12002),
    '.gov': ('localhost', 12003),
    '.in': ('localhost', 12004),
}
AUTH_SERVER_ADDRESS = {
    'ftp.google.com': ('localhost', 12011),
    'www.google.com': ('localhost', 12012),
    'ftp.uncc.edu': ('localhost', 12021),
    'www.uncc.edu': ('localhost', 12022),
    'ftp.nic.in': ('localhost', 12031),
    'www.nic.in': ('localhost', 12032),
}
CACHE = {}

# Define functions
def send_query(server_address, query):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(query.encode(), server_address)
        response, _ = sock.recvfrom(1024)
        return response.decode()

def resolve_hostname(hostname):
    if hostname in CACHE:
        print(f'Found {hostname} in cache')
        return CACHE[hostname]
    
    print(f'Querying root DNS server for {hostname}')
    tld_server_address = send_query(ROOT_SERVER_ADDRESS, hostname)
    print(f'Root DNS server returned {tld_server_address}')
    
    print(f'Querying {tld_server_address} for {hostname}')
    auth_server_address = send_query(TLD_SERVER_ADDRESS[tld_server_address], hostname)
    print(f'{tld_server_address} returned {auth_server_address}')
    
    print(f'Querying {auth_server_address} for {hostname}')
    ip_address = send_query(AUTH_SERVER_ADDRESS[hostname], hostname)
    print(f'{auth_server_address} returned {ip_address}')
    
    CACHE[hostname] = ip_address
    return ip_address

# Define main program
def main():
    while True:
        hostname = input('Enter a server name (or "bye" to quit): ')
        if hostname == 'bye':
            break
        ip_address = resolve_hostname(hostname)
        if ip_address:
            print(f'The IP address of {hostname} is {ip_address}')
        else:
            print(f'Could not resolve {hostname}')

if __name__ == '__main__':
    main()