#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-01 17:08:21
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

tcp_serv = socket(AF_INET,SOCK_STREAM) #tcp连接
tcp_serv.bind(ADDR) #绑定地址端口
tcp_serv.listen(5) #端口监听，最大5个

while True:
    print 'waiting for connection...'
    tcp_client,addr = tcp_serv.accept() #客户端连接
    print 'connect from {tcp_client},{addr}'.format(tcp_client=tcp_client,addr=addr)

    while True:
        data = tcp_client.recv(BUFSIZE)
        if not data:
            break
        tcp_client.send('[{ctime}] {data}'.format(ctime=ctime(),data=data))
    tcp_client.close()
tcp_serv.close()