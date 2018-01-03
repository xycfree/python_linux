#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-25 12:03:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from time import ctime
import random

'''
decorator 装饰器
'''

def tsfunc(func):
    def funcs():
        print '{t} {n}() called'.format(t=ctime(),n=func.__name__)
        return func()
    return funcs

@tsfunc
def foo():
    print 'fo_end ...'

foo()

#过滤器filter
def odd(n):
    return n % 2
allNums = []
for eachnum in range(9):

    allNums.append(random.randint(1,100))
print allNums
#print filter(odd, allNums)
print filter(lambda n:n%2, allNums) #匿名函数替代odd函数
print [n for n in allNums if n % 2] #通过列表进行判断过滤
#列表遍历随机生成的10位数字列表，并判断过滤
print [n for n in [random.randint(1,100) for i in range(9)] if n % 2]

print '##########'*5

def randGen(alist):
    while len(alist) > 0:
        yield alist.pop(random.randint(0,len(alist)))

#for item in randGen([1,3,'a','b']):
#    print item
print '中文'
li = [1,3,4,'a','b']
r = randGen(li)
for i in range(len(li),0,-1):
    print r.next()
