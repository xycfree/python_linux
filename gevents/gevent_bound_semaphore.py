#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/6/15 16:29
# Author: xycfree
# @Descript: gevent 的锁和信号量

import gevent
from gevent.pool import Pool
from gevent.lock import RLock, BoundedSemaphore

""" 信号量是一个允许greenlet相互合作，限制并发访问或运行的低层次的同步原语。信号量有二个方法acquire和release。
在信号量是否已经被acquire或release， 和拥有的资源的数量之间不同，被称为此信号量的范围。如果一个信号量的范围已经降低到0，
它会阻塞acquire操作直到另一个已经获得信号量的greenlet的释放 
信号量和锁常常用来保证资源只在程序上下文被单次使用
"""

sem = BoundedSemaphore(3)

def worker1(n):
    sem.acquire()  # 获取信号
    print('worker {} acquired semaphore'.format(n))
    gevent.sleep(0)
    sem.release()  # 释放信号
    print('worker {} released semaphore'.format(n))

def worker2(n):
    with sem:
        print('worker2 {} acquired seapore'.format(n))
        gevent.sleep(0)
    print('worker2 {} released semaphore'.format(n))

pool = Pool()
pool.map(worker1, range(0,2))
pool.map(worker2, range(3, 7))

