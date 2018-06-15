#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/4/6 19:20
# @Descript: 有序列表和二分查找

import bisect
import random


class SortList(list):
    def __init__(self, iterable):
        super(SortList, self).__init__(sorted(iterable))

    def insort(self, item):
        """插入并排序"""
        bisect.insort(self, item)

    def index(self, value, start=None, stop=None):
        place = bisect.bisect_left(self[start:stop],value)
        if start:
            place += start
        end = stop or len(self)
        if place < end and self[place] == value:
            return place
        raise ValueError('%s is not in list' % value)

if __name__ == '__main__':
    li = []
    for i in range(20):
        li.append(random.randint(1, 100))
    print(li)
    s = SortList(li)
    print(s)
    s.insort([1,3,12,12341,12])
    print(s)
