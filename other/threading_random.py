#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/6/1 15:05
# @Descript:

import threading
import random


def print_func(m):
    print(m)

t = []
for i in range(10):
    m = random.random()
    t.append(threading.Thread(target=print_func, args=(m,)))
for i in t:
    i.start()
for i in t:
    i.join()

