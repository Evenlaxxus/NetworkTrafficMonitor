import os

import pyshark
from graphviz import Digraph, Graph

from backend.connections import Packet, get_devices, local_devices


def sniffing():
    cap = pyshark.FileCapture('backend/dump.pcap')
    list_of_packets = []

    # Creating a list of packets from *.pcap file.
    for packet in cap:
        if "IP " in str(packet.layers):
            list_of_packets.append(Packet(packet['ip'].src, packet['ip'].dst, packet['ip'].ttl, packet['ip'].id))

    # Get addresses and print them
    get_devices(list_of_packets)
    #print("Local: ", local_devices)
    #print("Global: ", global_devices)
    return local_devices


def graf():
    local_devices = sniffing()
    addresses = []
    for local_device in local_devices:
        if local_device[0] not in addresses:
            addresses.append(local_device[0])
        if local_device[1] not in addresses:
            addresses.append(local_device[1])
    print(addresses)

    images = os.path.abspath('.\\images')
    dot = Digraph(comment='Network graph', format='png')
    #dot.attr('node', image="../../images/switch.png")
    dot.attr('node', shape='plaintext')
    dot.attr('node', arrowhead='none')
    for address in addresses:
        dot.node(address)
    #dot.node('A', 'Modem\n 192.168.0.1', image=images + '\\modem.png')
    #dot.edges(['AB', 'AE', 'BC', 'BD', 'EF', 'EG'])
    for local_device in local_devices:
        dot.edge(local_device[0], local_device[1])
    print(dot.source)
    dot.render('../graph-output/graph.gv')
    return '../graph-output/graph.gv.png'


if __name__ == "__main__":
    graf()
