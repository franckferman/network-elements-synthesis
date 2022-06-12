import sys
from sys import argv
from scapy.all import sr1, IP, TCP, conf

conf.verb=0
SYN=0x02
ACK=0x10
SYNACK=SYN|ACK

def Check_UserInput():
    if len(sys.argv)==1:
        host=str(input("Host: "))
        port=int(input("Port: "))
        print("")

    elif len(sys.argv)==2 or len(sys.argv)>3:
        print("\033[0;31mThree arguments are expected.\033[00m")
        exit(1)

    elif len(sys.argv)==3:
        host=str((sys.argv[1]))
        port=int((sys.argv[2]))

    syn_pkt=IP(dst=host)/TCP(dport=port,flags='S')
    synack_pkt=sr1(syn_pkt, timeout=1)

    if synack_pkt is None:
        print('\033[0;31mCannot reach host "%s" on port %d\033[00m' % (host, port))

    elif synack_pkt['TCP'].flags == SYNACK:
        print('PORT %4d is OPEN on host "%s"' % (port, host))

    else:
        print('PORT %4d is CLOSED on host "%s"' % (port, host))



if __name__ == '__main__':
    Check_UserInput()
