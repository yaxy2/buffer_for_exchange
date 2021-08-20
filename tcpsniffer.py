import socket
import datetime
import struct
import textwrap


HOST_IP = 'localhost'
PORT = 3000


def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((HOST_IP, PORT))
    conn.listen(10)

    while True:
        raw_data, addr = conn.recv(65536)
        dest_mac, src_mac, eth_proto = ethernet_frame(raw_data)
        print('\nEthernet Frame:')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))

#Unpack Ethernet Frame

def ethernet_frame(data):
    dest_mac, source_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(source_mac), socket.htons(proto), data[14:]


# Return MAC Adress | converted (MAC Dummy AA:BB:CC:DD:EE:FF)

def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()


main()
