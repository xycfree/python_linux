#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/11/28 15:46
# @Author  : xycfree
# @Link    : http://example.org
# @Version : $

import os

items = [{'name':'zhangsan','age':30},
    {'name':'lisi','age':20},
    {'name':'wangwu','age':32}]



it = sorted(items,key=lambda x:x['age'],reverse=True)
print(it)