#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/6/8 17:32
# Author: xycfree
# @Descript:

import asyncio
import time
# try:
#     import uvloop
#     asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# except:
#     pass


def get_ins_data():
    print('start')
    li = [i for i in range(1000000)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ins_main(li))
    print('start, end....')
    return "运行完毕"


async def ins_data(li):
    start = time.time()
    for i in li:
        # time.sleep(0.1)
        print(i)
    end = time.time()
    print("is_data Complete in {} seconds".format(end - start))


async def ins_data_1(li):
    start = time.time()
    for i in li:
        # time.sleep(0.1)
        print(i)
    end = time.time()
    print("is_data_1 Complete in {} seconds".format(end - start))


async def ins_main(li):
    start = time.time()
    await asyncio.wait([
        ins_data(li),
        # ins_data_1(li)
    ])
    end = time.time()
    print("Complete in {} seconds".format(end - start))


if __name__ == '__main__':
    res = get_ins_data()
    print(res)