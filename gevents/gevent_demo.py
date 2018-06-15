#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/6/6 12:02
# Author: xycfree
# @Descript:

import gevent
from eventlet import getcurrent
from gevent import get_hub, greenlet
from gevent._util import _NONE
from gevent.hub import Waiter


def test_1():
    print('切换不出去')
    print('切换出去我不是循环')
    gevent.sleep(1)

def test_2():
    print('切换')
    print('切换出去我去')
    gevent.sleep(3)

gevent.spawn(test_1)
gevent.spawn(test_2)
gevent.sleep(1)


from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
print('aa')
gr1.switch()
print('bb')

import random
from time import sleep
from greenlet import greenlet
from queue import Queue

queue = Queue(1)


@greenlet
def producer():
    chars = ['a', 'b', 'c', 'd', 'e']
    global queue
    while True:
        char = random.choice(chars)
        queue.put(char)
        print("Produced: ", char)
        sleep(1)
        consumer.switch()


@greenlet
def consumer():
    global queue
    while True:
        char = queue.get()
        print("Consumed: ", char)
        sleep(1)
        producer.switch()


if __name__ == "__main__":
    producer.run()
    consumer.run()
