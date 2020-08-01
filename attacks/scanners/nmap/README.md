## NMAP PCAPs

### Info

Port scanner. See: [nmap](https://github.com/nmap/nmap).

### PCAPs

+ nmap_80_all.pcap

  **Description**: TCP port 80 scan, followed by OS detection, version detection, script scanning, and traceroute.

  **Command**: `nmap -p 80 -A -v 130.211.223.103`

  **Version**:
  ```
  Nmap version 7.80 ( https://nmap.org )
  Platform: x86_64-pc-linux-gnu
  Compiled with: nmap-liblua-5.3.5 openssl-1.1.1d libz-1.2.11 libpcre-8.42 libpcap-1.9.1 nmap-libdnet-1.12 ipv6
  Compiled without: libssh2
  Available nsock engines: epoll poll select
  ```

+ nmap_80_w_service_detection.pcap

  **Description**: TCP port 80 scan, version detection.

  **Command**: `nmap -p 80 -sV 130.211.223.103`

  **Version**:
  ```
  Nmap version 7.80 ( https://nmap.org )
  Platform: x86_64-pc-linux-gnu
  Compiled with: nmap-liblua-5.3.5 openssl-1.1.1d libz-1.2.11 libpcre-8.42 libpcap-1.9.1 nmap-libdnet-1.12 ipv6
  Compiled without: libssh2
  Available nsock engines: epoll poll select
  ```

+ nmap_80_vanilla.pcap

  **Description**: TCP port 80 scan.

  **Command**: `nmap -p 80 130.211.223.103`

  **Version**:
  ```
  Nmap version 7.80 ( https://nmap.org )
  Platform: x86_64-pc-linux-gnu
  Compiled with: nmap-liblua-5.3.5 openssl-1.1.1d libz-1.2.11 libpcre-8.42 libpcap-1.9.1 nmap-libdnet-1.12 ipv6
  Compiled without: libssh2
  Available nsock engines: epoll poll select
  ```

