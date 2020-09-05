import os
import math
import pyshark
from graphviz import Digraph, Graph

from backend.connections import Packet, get_devices


def sniffing():
    cap = pyshark.FileCapture('backend/dump.pcap')
    list_of_packets = []

    # Creating a list of packets from *.pcap file.
    for packet in cap:
        if "IP " in str(packet.layers):
            list_of_packets.append(Packet(packet['ip'].src, packet['ip'].dst, packet['ip'].ttl, packet['ip'].id))

    # Get addresses and print them
    same_network, diff_network, local_devices, global_devices = get_devices(list_of_packets)
    #print("Local: ", local_devices)
    print("Global: ", global_devices)
    return local_devices, global_devices


def live():
    interfaces = ['Wi-Fi']
    cap = pyshark.LiveCapture(interface=interfaces, output_file='test.pcap')
    try:
        cap.sniff(timeout=10)
    except:
        print("timeout")
    cap.close()
    cap2 = pyshark.FileCapture('test.pcap')
    list_of_packets = []

    # Creating a list of packets from *.pcap file.
    for packet in cap2:
        if "IP " in str(packet.layers):
            list_of_packets.append(Packet(packet['ip'].src, packet['ip'].dst, packet['ip'].ttl, packet['ip'].id))

    # Get addresses and print them
    same_network, diff_network, local_devices, global_devices = get_devices(list_of_packets)
    #print("Local: ", local_devices)
    print("Global: ", global_devices)
    return local_devices, global_devices


def graf(scan_type):
    if scan_type == 'live':
        local_devices, global_devices = live()
    else:
        local_devices, global_devices = sniffing()
    addresses = []
    global_addresses = []
    for local_device in local_devices:
        if local_device[0] not in addresses:
            addresses.append(local_device[0])
        if local_device[1] not in addresses:
            addresses.append(local_device[1])
    for global_device in global_devices:
        if global_device[0] not in addresses:
            addresses.append(global_device[0])
            global_addresses.append(global_device[0])
        if global_device[1] not in addresses:
            addresses.append(global_device[1])
            global_addresses.append(global_device[1])
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
        dot.edge(local_device[0], local_device[1], color='blue')
    for global_device in global_devices:
        dot.edge(global_device[0], global_device[1], color='red')
    # subgraph for local network
    with dot.subgraph() as s:
        s.attr(rank='same')
        for n in local_devices:
            s.node(n[0])

    columns = math.floor(math.sqrt(len(global_addresses)))
    rows = math.ceil(len(global_addresses)/math.floor(math.sqrt(len(global_addresses))))
    # print(rows, columns)
    extract = (len(global_addresses) % math.floor(math.sqrt(len(global_addresses))))
    # print(extract)
    # print(global_addresses)

    global_address_matrix = [[] for i in range(rows)]

    for i in range(0, rows-1):
        for j in range(0, len(global_addresses)-extract, columns):
            global_address_matrix[i].append(global_addresses[j])

    # NOT WORKING!!!!
    # subgraph for global network
    for i in range(0, rows - 1):
        with dot.subgraph() as s:
            s.attr(rank='same')
            for n in global_address_matrix[i]:
                s.node(n)


    print(dot.source)
    dot.render('../graph-output/graph.gv')
    return '../graph-output/graph.gv.png'


if __name__ == "__main__":
    graf()
