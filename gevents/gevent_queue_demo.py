#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/6/13 11:40
# Author: xycfree
# @Descript: greenlets互相通信之Queue
"""
1.Queue 模块实现了多生产者、多消费者队列
它特别适用于信息必须在多个线程间安全地交换的多线程程序中。这个模块中的 Queue 类实现了所有必须的锁语义；
2.模块实现了三类队列，主要差别在于取得数据的顺序上
FIFO队列中，最早加入的任务会被最先得到。LIFO队列中，最后加入的任务会被最先得到（就像栈一样）。在优先队列中，任务被保持有序，拥有最小值的任务（优先级最高）被最先得到；
3.python内置Queue特点：
虽然线程安全，但同步线程开销；
4.gevent中Queue
1）Queue(先进先出)；
2）LifoQueue(先进后出)；
3）PriorityQueue(优先级队列)。
5.gevent中Queue特点
无线程同步开销，但有Greenlet之间的线程内同步，无法线程间操作。
"""

import time
import gevent
from gevent.queue import Queue, Empty, LifoQueue, PriorityQueue

class Job(object):

    def __init__(self, priority, desc):
        self.priority = priority
        self.desc = desc

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return "priority {} desc {}!".format(self.priority, self.desc)

def read_queue():
    q = PriorityQueue()
    q.put(Job(2, 'gaga'))
    q.put(Job(3, 'haha'))
    q.put(Job(6, 'xixi'))
    q.put(Job(1, 'hehe'))
    q.put(Job(10, 'heihei'))
    while not q.empty():
        _job = q.get()
        print(_job)
    time.sleep(1)
    print('wait...')

read_queue()

tasks = Queue()

def boss():
    for i in range(1, 10):
        tasks.put_nowait(i)

def worker(n):
    try:
        while True:
            task = tasks.get(timeout=1)
            # task = tasks.get()
            print('worker {} got task {}'.format(n, task))
            gevent.sleep(0)
    except Empty:
        print('quit')

gevent.spawn(boss).join()
gevent.joinall([
    gevent.spawn(worker, 'mm'),
    gevent.spawn(worker, 'nn'),
    gevent.spawn(worker, 'bb'),
    gevent.spawn(worker, 'vv'),
])