#!/usr/bin/env python
#coding:utf-8
from twisted.python.compat import raw_input

__author__ = 'xycfree'
from socket import *
#端口扫描
if __name__ == '__main__':
    target = raw_input('Enter host to scan: ')
    targetIP = gethostbyname(target)
    print('Starting scan on host ', targetIP)

    #scan reserved ports
    for i in range(20, 1025):
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((targetIP, i))

        if(result == 0) :
            print('Port %d: OPEN' % (i,))
        s.close()
