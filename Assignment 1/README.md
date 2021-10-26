# ARP-Spoofing

ARP spoofing is a type of attack in which a malicious actor sends falsified ARP (Address Resolution Protocol) messages over a local area network. This results in the linking of an attacker’s MAC address with the IP address of a legitimate computer or server on the network. Once the attacker’s MAC address is connected to an authentic IP address, the attacker will begin receiving any data that is intended for that IP address. ARP spoofing can enable malicious parties to intercept, modify or even stop data-in-transit. ARP spoofing attacks can only occur on local area networks that utilize the Address Resolution Protocol. We have developed two scripts - for starting an ARP SPoof Attack and another for Detecting an ARP attack and then blocking any such ARP packets from coming through.

## Requirements & Prerequisites

1. Linux OS(Preffered)
2. Python
3. GCC Compiler

## Instructions

#### Insertion

Run the following command to start the ARP Spoofer script :
`sudo python Insertion/arpspoof.py {Target_IP} -f`
And enter the password for root user

#### Detection & Blocking

**NOTE: Make sure you run the defender script first and then the ARP Spoof script if you are
running both**
Run the following commands :

```
gcc -o Detection_Removal/builds/defender Detection_Removal/src/defender.c -lpcap -pthread
sudo Detection_Removal/builds/defender
```

## Contributors

1. Harshdeep Singh
2. Prasanth Kota
