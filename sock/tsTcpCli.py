#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-01 17:18:00
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcp_clie = socket(AF_INET,SOCK_STREAM) #创建tcp连接
tcp_clie.connect(ADDR) #连接服务端

while True:
    data = raw_input("input data >:")
    if not data:
        break
    tcp_clie.send(data) #向服务端发送数据
    data = tcp_clie.recv(BUFSIZE) #接收服务端返回的数据
    if not data:
        break
    print 'Server is back info: {data}'.format(data=data)
tcp_clie.close()