#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/6/13 14:56
# Author: xycfree
# @Descript: 管理多个Greenelet
import random
import time

import gevent
import requests
from gevent.pool import Group, Pool
from gevent.queue import Queue

group = Group()


class RandQueue(Queue):
    def __init__(self, maxsize, items=None):
        self.maxsize = maxsize
        self.queue = []

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        return self.queue.pop(random.randint(0, len(self.queue) - 1))


q = RandQueue(10)
for i in range(20):
    q._put(i)
print(q._get())


def talk(msg):
    for i in range(3):
        print(i, msg)


g1 = gevent.spawn(talk, 'bar')
g2 = gevent.spawn(talk, 'foo')
group.add(g1)
group.add(g2)
group.add(gevent.spawn(talk, 'hello'))
print(group)
group.join()


def intensive(n):
    gevent.sleep(3 - n)
    return 'task, {}'.format(n)


imap_data = group.imap(intensive, range(3))
for i in imap_data:
    print(i)

print('==============')
pool = Pool(2)


def down(url):
    print(len(requests.get(url).content.decode('utf-8')))


urls = ['http://www.maiziedu.com/', 'http://www.iqiyi.com/'
    , 'http://www.baidu.com/', 'http://www.iteye.com/']
group = Group()
for i in urls:
    pool.spawn(down, i)
t1 = time.time()
pool.join()
print('use ', time.time() - t1)
