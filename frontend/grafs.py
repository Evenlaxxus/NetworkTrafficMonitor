import pyshark
from graphviz import Digraph, Graph

def sniffing():
    cap = pyshark.LiveCapture(interface="Ethernet")
    # cap.sniff(timeout=50)
    for packet in cap.sniff_continuously(packet_count=5):
        print('Just arrived:', packet)


def graf():
    dot = Digraph(comment='The Round Table')
    dot.attr('node', image="switch.png")
    dot.attr('node', shape='plaintext')
    dot.attr('node', arrowhead='none')
    dot.node('A', '192.168.0.1')
    dot.node('B', '192.168.0.2')
    dot.node('L', '192.168.0.3')
    dot.edges(['AB', 'AL'])
    dot.edge('B', 'L', constraint='false')
    print(dot.source)
    dot.render('test-output/round-table.gv', view=True)