#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/6/13 10:24
# Author: xycfree
# @Descript: greenlets互相通信，使用 Event 和 AsyncResult

import gevent
from gevent.event import Event, AsyncResult
# evt = Event()
# is_ok = '太好喝了'
evt = AsyncResult()

def setter():
    print('上午上班好困...')
    gevent.sleep(3)
    print('好吧，来杯咖啡吧!')

    # print(is_ok)
    # global evt, is_ok
    # is_ok = "这一杯, 谁不爱"
    # evt.set()

    global evt
    evt.set("这一杯, 谁不爱")


def waiter():
    print('怎么办?')
    # gevent.sleep(0)
    # global evt, is_ok
    # evt.wait()
    # print(is_ok)

    global evt
    data = evt.get()
    print(data)
    print('神清气爽啦!')


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter)
    ])