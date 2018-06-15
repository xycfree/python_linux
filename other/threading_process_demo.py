#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/4/7 13:56
# @Descript: 多线程，多进程比较
import multiprocessing
import random
import threading

result = []


def compute():
    result.append(sum([random.randint(1, 100) for i in range(1000000)]))


def threading_start():
    workers = [threading.Thread(target=compute) for i in range(8)]

    for i in workers:
        i.start()
    for i in workers:
        i.join()
    print('result: {}'.format(result))


def multiprocessing_start():
    pool = multiprocessing.Pool(2)
    res = pool.map(compute, range(8))
    print('result: {}'.format(res))

multiprocessing_start()

