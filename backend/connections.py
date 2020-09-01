from collections import namedtuple
import pyshark

# Creating a named tuple
Pair = namedtuple("Pair", ['src', 'dst'])


class Packet:
    # Definition of a packet.
    def __init__(self, source, destination, time_to_live, identification):
        self.src = source
        self.dst = destination
        self.ttl = time_to_live
        self.id = identification
        self.pair = Pair(self.src, self.dst)

    # print packet information
    def get_packet_info(self):
        print(self.pair, self.ttl, self.id)


# variables for devices
local_devices = []
global_devices = []


# get unique addresses
def get_devices(list_of_packets):
    same_network, diff_network = [], []

    # checking 255.255.255.0
    for p in list_of_packets:
        s = p.pair[0].split(".", 3)
        d = p.pair[1].split(".", 3)

        # if network is the same put address to local devices list
        if s[0:3] == d[0:3]:
            if p.pair not in same_network:
                same_network.append(p.pair)
                if s not in local_devices:
                    local_devices.append(s)

        # else put to global devices list
        else:
            if p.pair not in diff_network:
                diff_network.append(p.pair)
                if s not in global_devices and s[0:2] != ['192', '168']:
                    global_devices.append(s)
    return same_network, diff_network


# Reading *.pcap file.
# TODO: file path
# TODO: LiveCapture
pcap = pyshark.FileCapture('dump.pcap')

list_of_packets = []

# Creating a list of packets from *.pcap file.
for packet in pcap:
    if "IP " in str(packet.layers):
        list_of_packets.append(Packet(packet['ip'].src, packet['ip'].dst, packet['ip'].ttl, packet['ip'].id))

# Get addresses and print them
get_devices(list_of_packets)
print("Local: ", local_devices)
print("Global: ", global_devices)
