#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/2/15 15:15
# @Descript: 斐波那契数列生成器

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibon(100):
    print(x)