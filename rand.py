#!/usr/bin/env python
from __future__ import unicode_literals
# -*- coding: utf-8 -*-
# @Date    : 2016-07-23 17:25:03
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import sys
import random
print sys.stdin.encoding
print sys.stdout.encoding

a = ['王', '丁', '波', '翀', '小', '果']
# print a
b = tuple(a)
# print b
for i in b:
    print i,
print '\n'
rand = random.choice(a)
print '选中的幸运顾客:{rand},获得奖金为:{money}'.format(rand=rand, money=500000)
