from collections import namedtuple
import pyshark

#Creating a named tuple
Pair = namedtuple("Pair", ['src', 'dst'])


class Packet:
#Definition of a packet.
    def __init__(self, source, destination, timeToLive, identification ):
        self.src = source
        self.dst = destination
        self.ttl = timeToLive
        self.id = identification
        self.pair = Pair(self.src, self.dst)

#Sorting list od packets.
def sort(list_of_packets):
    same_Network, diff_Network = [], []

    #It splits source and destination addresses in every pair and checks if their first 3 octets are the same.
    #Then adds pairs to one of two lists depends on a condition result.
    for p in list_of_packets:
        s = p.pair[0].split(".", 3)
        d = p.pair[1].split(".", 3)
        if s[0:3] == d[0:3]:
           same_Network.append(p)
        else:
            diff_Network.append(p)
    print("DIFFERENT NET")
    print(diff_Network)
    print("SAME NET")
    print(same_Network)

#Reading *.pcap file.
pcap = pyshark.FileCapture('dump.pcap')

id = []

#Creating a list of packets from *.pcap file.
for packet in pcap:
    if "IP " in str(packet.layers):
        id.append(Packet(packet['ip'].src, packet['ip'].dst, packet['ip'].ttl, packet['ip'].id))

#Sorting test.
print(sort(id))