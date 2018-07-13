#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/6/19 10:05
# Author: xycfree
# @Descript: gevent 子进程, 基于wait_write/wait_read的方法，在windows不工作

import gevent
from multiprocessing import Process, Pipe

from gevent._socketcommon import wait_read, wait_write

a, b = Pipe()
c, d = Pipe()

def relay():
    for i in range(10):
        msg = b.recv()
        c.send(msg + ' in ' + str(i))

def put_msg():
    for i in range(10):
        wait_write(a.fileno())
        a.send('hi')

def get_msg():
    for i in range(10):
        wait_read(d.fileno())
        print(d.recv())

if __name__ == '__main__':
    proc = Process(target=relay)
    proc.start()

    g1 = gevent.spawn(get_msg)
    g2 = gevent.spawn(put_msg)
    gevent.joinall([g1, g2], timeout=1)

