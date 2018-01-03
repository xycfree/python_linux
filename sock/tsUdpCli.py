#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-01 18:11:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

udp_clie =socket(AF_INET,SOCK_DGRAM)
while True:
    data = raw_input("input data >: ")
    if not data:
        break
    udp_clie.sendto(data,ADDR)
    data,ADDR = udp_clie.recvfrom(BUFSIZE)
    if not data:
        break
    print data

udp_clie.close()
