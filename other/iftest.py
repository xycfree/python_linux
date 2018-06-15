#!/usr/bin/env python
from __future__ import unicode_literals
# coding:utf-8

__author__ = 'xycfree'
import random
r = random.randint(1, 100)
print('random num is : ', r)
count = 5
while True:
    a = input("a=: ")
    if r != int(a):
        print("input error,input...:")
        count -= 1
        if count < 1:
            break  # 输入错误次数超过5次，退出

    else:
        print("input success!")
        break
