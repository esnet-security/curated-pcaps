#!/usr/bin/env python3

import itertools
import random
from scapy.all import *

tcp_flags = "U" # URG: Indicates that the Urgent pointer field is significant
tcp_flags += "A" # ACK: All packets after the initial SYN packet sent by the client should have this flag set.
tcp_flags += "P" # PSH: Push function. Asks to push the buffered data to the receiving application.
tcp_flags += "R" # RST: Reset the connection
tcp_flags += "S" # SYN: Synchronize sequence numbers. Only the first packet sent from each end should have this flag set.
tcp_flags += "F" # FIN: Last packet from sender

all_flag_combos = []

for i in range(len(tcp_flags)):
    for combo in itertools.combinations(tcp_flags, i):
        all_flag_combos.append(combo)

used_ports = []
def get_random_port():
    global used_ports
    port = random.randint(30000,60000)
    while port in used_ports:
        port = random.randint(30000,60000)
    used_ports.append(port)

    return port

src_ip = "10.0.0.10"
dest_ip = "10.0.0.80"
dest_port = 80

one_way_pkts = []
two_way_pkts = []

for orig_flags in all_flag_combos:
    port = get_random_port()
    orig_pkt = Ether()/IP(src=src_ip, dst=dest_ip)/TCP(sport=port,dport=dest_port,flags="".join(orig_flags))
    one_way_pkts.append(orig_pkt)

    o = "".join(orig_flags)
    if not o:
        o = "None"
    wrpcap("one_way_" + o + ".pcap", [orig_pkt])

    for resp_flags in all_flag_combos:
        port = get_random_port()
        orig_pkt = Ether()/IP(src=src_ip, dst=dest_ip)/TCP(sport=port,dport=dest_port,flags="".join(orig_flags))
        two_way_pkts.append(orig_pkt)
        resp_pkt = Ether()/IP(src=dest_ip, dst=src_ip)/TCP(sport=dest_port,dport=port,flags="".join(resp_flags))
        two_way_pkts.append(resp_pkt)

        r = "".join(resp_flags)
        if not r:
            r = "None"

        wrpcap("two_way_" + o + "_" + r + ".pcap", [orig_pkt, resp_pkt])

wrpcap('one_way_all_flags.pcap', one_way_pkts)
wrpcap('two_way_all_flags.pcap', two_way_pkts)
