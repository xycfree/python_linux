#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/10 17:20
# @Desc    : 测试join,+ 连接字符串的速度
import timeit  # 生成测试所需要的字符数组

str_list = ['it is a long value string will not keep in memory' for i in range(10000)]

def join_test():
    return ''.join(str_list)

def plus_test():
    result = ''
    for i, v in enumerate(str_list):
        result += v
    return result

if __name__ == '__main__':
    jointimer = timeit.Timer('join_test()','from __main__ import join_test')
    print(jointimer.timeit(number=10000))
    plustimer = timeit.Timer('plus_test()', 'from __main__ import plus_test')
    print(plustimer.timeit(number=10000))