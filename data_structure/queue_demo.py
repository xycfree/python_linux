#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/6/7 17:41
# Author: xycfree
# @Descript:

from queue import Queue
from queue import deque

def hot_potato(name_list, num):
    """传土豆游戏"""
    q = Queue()

    for name in name_list:
        print(name)
        q.put(name)

    while q.qsize() > 1:
        for i in range(num):
            _put = q.get()
            print('put: {}'.format(_put))
            q.put(_put)
        _get = q.get()
        print(_get)

    return q.get()


if __name__ == '__main__':
    print(hot_potato(['a', 'aa', 'bb', 'bba', 'cc', 'dd'], 7))
