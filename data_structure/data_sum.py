#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/6/7 15:31
# Author: xycfree
# @Descript:

import time
import timeit
from timeit import Timer

def data_sums(num):
    start_time = time.time()
    total = 0
    for i in range(num):
        temp = i
        total = total + temp

    end_time = time.time()
    execute_time = end_time - start_time
    print('total: {}, execute time: {}'.format(total, execute_time))
    return total


def data_sums_1(num):
    start_time = time.time()
    total = 0
    for i in range(num):
        total += i
    end_time = time.time()
    execute_time = end_time - start_time
    print('total: {}, execute time: {}'.format(total, execute_time))
    return total


def data_sums_2(num):
    start_time = time.time()
    total = (num * (num - 1)) / 2
    end_time = time.time()
    execute_time = end_time - start_time
    print('total: {}, execute time: {}'.format(total, execute_time))
    return total

def test_list_1(num):
    start_time = time.time()
    li = []
    for i in range(num):
        li = li + [i]

    end_time = time.time()
    execute_time = end_time - start_time
    print('total: {}, execute time: {}'.format(sum(li), execute_time))


def test_list_2(num):
    start_time = time.time()
    li = []
    for i in range(num):
        li.append(i)
    end_time = time.time()
    execute_time = end_time - start_time
    print('total: {}, execute time: {}'.format(sum(li), execute_time))


def test_list_3(num):
    start_time = time.time()
    li = [i for i in range(num)]
    end_time = time.time()
    execute_time = end_time - start_time
    print('total: {}, execute time: {}'.format(sum(li), execute_time))


def test_list_4(num):
    start_time = time.time()
    li = list(range(num))
    end_time = time.time()
    execute_time = end_time - start_time
    print('total: {}, execute time: {}'.format(sum(li), execute_time))



if __name__ == '__main__':
    num = 100000
    # data_sums(50000000)
    # data_sums_1(50000000)
    # data_sums_2(50000000)
    test_list_1(num)
    test_list_2(num)
    test_list_3(num)
    test_list_4(num)

    # 使用timeit模块，查看一个方法执行的时间
    t1 = Timer("test_list_1", "from __main__ import test_list_1")
    print("concat ", t1.timeit(number=10000), "millliseconds")

    pop_zero = Timer("x.pop(0)", "from __main__ import x")
    pop_end = Timer("x.pop()", "from __main__ import x")

    x = list(range(num))
    print(pop_zero.timeit(number=1000))

    x = list(range(num))
    print(pop_end.timeit(number=1000))

