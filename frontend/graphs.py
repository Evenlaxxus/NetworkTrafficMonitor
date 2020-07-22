import pyshark
from graphviz import Digraph, Graph

def sniffing():
    cap = pyshark.LiveCapture(interface="Ethernet")
    # cap.sniff(timeout=50)
    for packet in cap.sniff_continuously(packet_count=5):
        print('Just arrived:', packet)


def graf():
    dot = Digraph(comment='The Round Table')
    #dot.attr('node', image="../../images/switch.png")
    dot.attr('node', shape='plaintext')
    dot.attr('node', arrowhead='none')
    dot.node('A', 'Modem 192.168.0.1', image='../../images/modem.png')
    dot.node('B', 'Router 192.168.0.2', image='../../images/router.png')
    dot.node('C', 'Computer 192.168.0.3', image='../../images/computer.png')
    dot.node('D', 'Computer 192.168.0.4', image='../../images/computer.png')
    dot.node('E', 'Router 192.168.0.5', image='../../images/router.png')
    dot.node('F', 'Computer 192.168.0.6', image='../../images/computer.png')
    dot.node('G', 'Computer 192.168.0.7', image='../../images/computer.png')
    dot.edges(['AB', 'AE', 'BC', 'BD', 'EF', 'EG'])
    print(dot.source)
    dot.render('test-output/graph.gv', view=True)


if __name__ == "__main__":
    graf()
