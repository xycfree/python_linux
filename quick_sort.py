#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-30 12:07:10
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

def quick_sort(arr):
    """
    快速排序方法,同理列表sorted()
    """
    if not arr:
        return []
    pivots = [x for x in arr if x == arr[0]]
    lesser = quick_sort([x for x in arr if x < arr[0]])
    greater = quick_sort([x for x in arr if x > arr[0]])

    return lesser + pivots + greater

arr = [7,2,3,1,6,9,11,22,34,34,65]
sort_arr = quick_sort(arr)
print sort_arr

print sorted(arr,reverse=True)

print(dict.fromkeys(arr).keys()) #列表去重
print(list(set(arr))) #列表去重

ids = [1,2,3,3,4,2,3,4,5,6,1]
news_ids = []
for id in ids:
    if id not in news_ids:
        news_ids.append(id)

print news_ids
