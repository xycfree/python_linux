#!/usr/bin/env/python
#coding:utf-8
__author__ = 'xycfree'

try:
    f = open('foo','r')
except IOError as e:
    print "IOError : " , e
else:
    data = f.read()
    f.close()

def add(x,y):
    return x + y

print add(3,6)

