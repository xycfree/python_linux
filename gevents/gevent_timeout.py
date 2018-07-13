#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/6/15 15:37
# Author: xycfree
# @Descript:

import gevent
from gevent import Timeout

seconds = 3
timeout = Timeout(seconds)

def wait():
    gevent.sleep(5)

try:
    print('gevent.spawn(wait)')
    gevent.spawn(wait).join()
except Exception as e:
    print('could not complete: {}'.format(e))


# import gevent
# from gevent import Timeout
# time_to_wait = 3  # seconds
#
# class TooLong(Exception):
#     pass
#
# with Timeout(time_to_wait, TooLong):
#     gevent.sleep(5)


import gevent
from gevent import Timeout

def wait():
    gevent.sleep(2)
timer = Timeout(1).start()
thread1 = gevent.spawn(wait)
try:
    thread1.join(timeout=timer)
except Timeout:
    print('Thread 1 timed out')

timer = Timeout.start_new(1)
thread2 = gevent.spawn(wait)
try:
    thread2.get(timeout=timer)
except Timeout:
    print('Thread 2 timed out')
