#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/13 15:34

import json
from collections import defaultdict

path = r'D:\pyworkspace\pydata-book-master\ch02\usagov_bitly_data2012-03-16-1331923249.txt'
record = [json.loads(line) for line in open(path)]
print(record[0]['tz'])
time_zones = [rec['tz'] for rec in record if 'tz' in rec]
print time_zones[:10]

def get_counts(sequence):
    counts = defaultdict(int)  # 所有值初始化为0
    for x in sequence:
        counts[x] += 1
    return counts

def top_counts(count_dict, n=10):
    value_key_paris = [(count, tz) for tz, count in count_dict.items()]
    value_key_paris.sort()  # 按value值对列表中的元祖进行排序
    return value_key_paris[-n:]

from collections import Counter
counts = Counter(time_zones)
print('###########'*10)
print(counts.most_common(10))  # 字典排序，倒叙

counts = get_counts(time_zones)
print(counts)
print(counts['America/New_York'])
print('###########'*10)
print top_counts(counts)
