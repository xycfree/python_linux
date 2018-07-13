#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/7/12 17:59
# Author: xycfree
# @Descript:

from concurrent import futures
from time import sleep

import requests


def printer(n):
    sleep(n)
    print("sleep {}s output {}".format(n, n))
    return n * n


executor = futures.ThreadPoolExecutor(max_workers=3)
results = executor.map(printer, [4, 3, 2, 1, 0])
print([i for i in results])

for i, result in enumerate(results):
    print('done ! result {}: {}'.format(i, result))

URLS = ['http://www.baidu.com/',
        'http://www.sina.com/',
        'http://www.mi.com/',
        'http://jd.com/',
        'http://taobao.com/']


def load_url(url, timeout):
    conn = requests.get(url, timeout=timeout)
    return conn.content.decode('utf-8')


with futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    print(future_to_url)
for future in futures.as_completed(future_to_url):
    url = future_to_url[future]
    try:
        data = future.result()
    except Exception as exc:
        print('%r generated an exception: %s' % (url, exc))
    else:
        print('%r page is %d bytes' % (url, len(data)))
