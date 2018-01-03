#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/10/23 21:08
# @Author  : xycfree
# @Link    : http://example.org
# @Version : $

import os
import random

li = []
for i in range(20):
    li.append(random.randint(1, 100))
print(li)


# 冒泡排序
def bubble_sort(li):  # 无序列表
    lens = len(li)  # 列表长度
    for i in range(lens):
        for j in range(i):
            if li[j] > li[i]:
                li[j], li[i] = li[i], li[j]
    return li


# 插入排序
def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


if __name__ == '__main__':
    print(bubble_sort(li))
    print(insert_sort(li))
