# -*- coding:utf8 -*-

import socket
import os
import sys
import re




def reply_to_iplist(data):
    # assert isinstance(data, str())
    iplist = ['.'.join(str(ord(x)) for x in s) for s in re.findall('\xc0.\x00\x01\x00\x01.{6}(.{4})', data.decode("gbk",error='ignore')) if all(ord(x) <= 255 for x in s)]
    return iplist

def domain_to_ip(dnsserver,domain):
    dnsserver = dnsserver
    seqid = os.urandom(2)
    host = ''.join(chr(len(x))+x for x in domain.split('.'))
    data = '%s\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00%s\x00\x00\x01\x00\x01' % (seqid, host)
    print(data)
    sock = socket.socket(socket.AF_INET,type=socket.SOCK_DGRAM)
    sock.settimeout(None)
    sock.sendto(data.encode(encoding="gbk"), (dnsserver, 53))
    print("****************6")
    data = sock.recvfrom(512)[0]
    print("****************7")
    print(type(data))
    print(data)
    return reply_to_iplist(data)

# dnsServer = "114.114.114.114"
dnsServer = "10.11.10.5"


def main(argv):
    print(argv)
    if len(argv)!=2:
        print('please follow a host name! \neg:python dns_client.py baidu.com')
    else:
        p = domain_to_ip(dnsServer,argv[1])
        print ("the ip address of "+argv[1]+" are as follows")
        print (p)
if __name__ == '__main__':
    main(sys.argv)