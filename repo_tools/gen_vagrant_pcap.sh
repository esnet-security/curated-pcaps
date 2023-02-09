#!/bin/sh

rm vagrant.pcap 2> /dev/null
vagrant destroy -f 2> /dev/null

vagrant up

# Wait up to 5 minutes
COUNTER=0
while [  $COUNTER -lt 300 ]; do
    if [ -f done ]; then
        rm done
        break
    fi
    let COUNTER=COUNTER+1
    sleep 1
done
exit
vagrant destroy -f

rm *-console.log
if [ -f tcpdump.filter ]; then
    tcpdump -r vagrant.pcap -F tcpdump.filter -w tmp.pcap
    mv tmp.pcap vagrant.pcap
fi
