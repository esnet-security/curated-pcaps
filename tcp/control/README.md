## TCP Control Flag PCAPs

### Info

These PCAPs attempt to include all TCP flag options, among the following flags:

+ SYN
+ ACK
+ FIN
+ RST
+ URG
+ PSH

Some congestion-related flags are not included.

These PCAPs were artificially created with Scapy, via [generate.py](./generate.py).

### Exhaustive PCAPs

+ `one_way_all_flags.pcap`

  **Description**: In each connection, one host (the client) sends a single packet to another host (the server) on TCP port 80. Each connection uses a different combination of TCP flags.

+ `two_way_all_flags.pcap`

  **Description**: In each connection, one host (the client) sends a single packet to another host (the server) on TCP port 80, and then the server sends a single packet back. Each connection uses a different combination of TCP flags.

### Selected PCAPs

These export only one or more packets from the PCAPs above.

+ `single_rst.pcap`

  **Description**: One packet, with the `RST` flag set, no response.

+ `single_syn.pcap`

  **Description**: One packet, with the `SYN` flag set, no response.

+ `single_syn_ack.pcap`

  **Description**: One packet, with the `SYN` and `ACK` flags set, no response.
