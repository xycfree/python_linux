#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-01 18:10:52
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

udp_serv = socket(AF_INET,SOCK_DGRAM)
udp_serv.bind(ADDR)

while True:
    print 'waiting for message...'
    data,addr = udp_serv.recvfrom(BUFSIZE)
    print data,addr
    udp_serv.sendto('[{ctime} {data}]'.format(ctime=ctime(),data=data),addr)

    print 'received from and returned to:',addr
udp_serv.close()