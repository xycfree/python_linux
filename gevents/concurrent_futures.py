#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/7/12 17:21
# Author: xycfree
# @Descript:

from concurrent.futures import ThreadPoolExecutor as Pool
from concurrent.futures import ProcessPoolExecutor as Pool
from concurrent.futures import as_completed
import requests
"""
Future
Future可以理解为一个在未来完成的操作，这是异步编程的基础。通常情况下，我们执行io操作，访问url时（如下）在等待结果返回之前
会产生阻塞，cpu不能做其他事情，而Future的引入帮助我们在等待的这段时间可以完成其他的操作。
"""
URLS = ['http://qq.com', 'http://sina.com', 'http://www.baidu.com', ]


def task(url, timeout=10):
    return requests.get(url, timeout=timeout)


with Pool(max_workers=3) as executor:
    future_tasks = [executor.submit(task, url) for url in URLS]

    for f in future_tasks:
        if f.running():
            print('%s is running' % str(f))

    for f in as_completed(future_tasks):
        try:
            ret = f.done()
            if ret:
                f_ret = f.result()
                print('%s, done, result: %s, %s' % (str(f), f_ret.url, len(f_ret.content)))
        except Exception as e:
            f.cancel()
            print(str(e))


"""
wait
wait方法接会返回一个tuple(元组)，tuple中包含两个set(集合)，一个是completed(已完成的)另外一个是uncompleted(未完成的)。
使用wait方法的一个优势就是获得更大的自由度，它接收三个参数FIRST_COMPLETED, FIRST_EXCEPTION和ALL_COMPLETE，
默认设置为ALL_COMPLETED。
wait有timeout和return_when两个参数可以设置。 
timeout控制wait()方法返回前等待的时间。 
return_when决定方法什么时间点返回：如果采用默认的ALL_COMPLETED，程序会阻塞直到线程池里面的所有任务都完成；
如果采用FIRST_COMPLETED参数，程序并不会等到线程池里面所有的任务都完成。
"""

# # coding: utf-8
# from concurrent.futures import ThreadPoolExecutor as Pool
# from concurrent.futures import wait
# import requests
#
# URLS = ['http://qq.com', 'http://sina.com', 'http://www.baidu.com', ]
#
#
# def task(url, timeout=10):
#     return requests.get(url, timeout=timeout)
#
#
# with Pool(max_workers=3) as executor:
#     future_tasks = [executor.submit(task, url) for url in URLS]
#
#     for f in future_tasks:
#         if f.running():
#             print('%s is running' % str(f))
#
#     results = wait(future_tasks)
#     done = results[0]
#     for x in done:
#         print(x)