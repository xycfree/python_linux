#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/6/8 15:47
# Author: xycfree
# @Descript:

def hello():
    try:
        a = 'hello'
        return a
    except:
        a = 'world'
        return a
    finally:
        print('aaaaaaaaaaaaa')

if __name__ == '__main__':
    res = hello()
    print(res)