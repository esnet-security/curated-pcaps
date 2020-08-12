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

### PCAPs

+ `one_way_all_flags.pcap`

  **Description**: In each connection, one host (the client) sends a single packet to another host (the server) on TCP port 80. Each connection uses a different combination of TCP flags.

+ `two_way_all_flags.pcap`

  **Description**: In each connection, one host (the client) sends a single packet to another host (the server) on TCP port 80, and then the server sends a single packet back. Each connection uses a different combination of TCP flags.

