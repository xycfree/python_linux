#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/13 17:46

import json
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from matplotlib import *

path = r'D:\pyworkspace\pydata-book-master\ch02\usagov_bitly_data2012-03-16-1331923249.txt'
record = [json.loads(line) for line in open(path)]

frame = DataFrame(record)
print(frame)
print(frame['tz'][:10])

tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])
tz_counts[:10].plot(kind='barh', rot=0)

results = Series([x.split()[0] for x in frame.a.dropna()])
print('#########'*10)
print(results[:5])

print('#########'*10)
print(results.value_counts()[:8])

print('#########'*10)
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
print(operating_system)

by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
print('#########'*10)
print(agg_counts)


indexer = agg_counts.sum(1).argsort()  # 按升序排序
print('#########'*10)
print(indexer[:10])

count_subset = agg_counts.take(indexer)[-10:]
print('#########'*10)
print(count_subset)
count_subset.plot(kind='barh', stacked=True)