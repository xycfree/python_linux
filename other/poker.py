#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-02 10:53:19
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import random
'''
扑克牌发牌，4个人，每人13张扑克牌
'''
pokers=range(52)
poke = []
random.shuffle(pokers) #打乱顺序
cloth = ['黑','红','梅','方']
poker_li=['A','2','3','4','5','6','7','8','9','10','J','Q','K']

for i in pokers:
    k,j=divmod(i, 13)
    poke.append(cloth[k]+poker_li[j])

play1 = tuple(poke[:13])
play2 = tuple(poke[13:26])
play3 = tuple(poke[26:39])
play4 = tuple(poke[39:])
p=[play1,play2,play3,play4]
for k,j in enumerate(p):
    print '第{k}个玩家：'.format(k=k+1),
    for i in j:
        print i,
    print '\n'




    






