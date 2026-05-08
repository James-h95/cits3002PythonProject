class Layer4:
    #Transport Layer(UDP segment)
    #new test nanasa 
    def __init__(self, src_port, dst_port, data):
        self.src_port = src_port
        self.dst_port = dst_port
        self.data = data
        
    """Segmentation & Encapsulation: Encapsulate application data into a UDP-like segment before transmission.
        Port-based Communication: Use source and destination port numbers to identify sending and receiving applications.
        Length Handling: Compute and include the total segment length (header + data).
        Checksum / Error Detection:
        Compute a checksum for each segment
        Verify the checksum at the receiver
        Discard corrupted segments
        Reliable Data Transfer (rdt2.2 – Alternating Bit Protocol):
        Use a sequence number (0 or 1) for each DATA segment
        The sender alternates sequence numbers: 0 → 1 → 0 → 1
        Upon receiving a valid DATA segment:
        The receiver delivers the data to the application
        The receiver sends an ACK with the same sequence number
        segment is corrupted or a duplicate:
        The receiver re-sends the last ACK
        The sender:
        Waits for the correct ACK
        incorrect or duplicate ACK is received, the sender retransmits the current segment
        Data Delivery: Deliver valid data to the application layer at the receiver.
    """

class Layer3:
    #Network Layer(IP packet)
    def __init__(self, src_ip, dst_ip, payload):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.payload = payload #from Layer4
        
    """Encapsulation: Encapsulate the Layer 4 segment into an IP-like packet before transmission.
        Addressing: Use source and destination IP addresses to identify hosts across networks.
        Routing / Forwarding: Routers must forward packets based on a routing table. Each node must maintain a routing table that maps the destination IP address to the outgoing interface and the next-hop IP addresses. This table is used to determine how packets are forwarded. As an example, when R1 receives the packet on Interface 1 from host A, it reads the destination IP address (10.0.2.20) and performs a routing table lookup. It finds that the destination network (10.0.2.0/24) is directly connected via Interface 2 (10.0.2.1). Since the destination is on a directly connected network, the next-hop IP is set to the destination IP itself (10.0.2.20). The router then selects Interface 2 as the outgoing interface and forwards the packet to the data link layer along with the next hop IP address and the selected interface for transmission.
        TTL Handling:
        Decrement TTL at each router
        Drop the packet if TTL reaches 0
        Packet Delivery: Deliver valid payload (UDP-like segment) to Layer 4 at the destination host.
    """

class Layer2:
    #Data-Link Layer (Ethernet frame)
    def __init__(self, src_mac, dst_mac, payload):
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        self.payload = payload #from Layer3
        
    """*Framing & Encapsulation: Encapsulate the Layer 3 packet into a frame before transmission.
        *MAC Addressing: Use source and destination MAC addresses to deliver frames within the local network. Each node must maintain a table that maps the next hop IP address (provided by the network layer) to the MAC addresses. This table is used to determine the destination MAC address when sending a frame.
        *Switching / Forwarding: o Learn the incoming source MAC address from received frames o Forward frames to the destination MAC address
        *Frame Delivery: Deliver valid payload (IP packet) to Layer 3 at the receiver.
    """
