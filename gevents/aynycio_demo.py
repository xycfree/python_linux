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
    li = [i for i in range(100000)]
    loop = asyncio.get_event_loop()  # 得到一个标准的事件循环
    # loop.run_until_complete(ins_main(li))  # 运行协同程序

    # 通过它可以获取一个协同程序的列表，同时返回一个将它们全包括在内的单独的协同程序，所以我们可以这样写
    loop.run_until_complete(asyncio.wait([ins_data(li),
                                          ins_data_1(li)]))

    # 通过它可以获取一个协同程序的列表，同时返回一个按完成顺序生成协同程序的迭代器，因此当你用它迭代时，会尽快得到每个可用的结果
    # loop.run_until_complete(asyncio.as_completed([ins_data(li),
    #                                       ins_data_1(li)]))
    loop.close()
    print('start, end....')
    return "运行完毕"


async def ins_data(li):
    start = time.time()
    for i in li:
        print(i)
        # await asyncio.sleep(0)  #  替换为await yield from asyncio.sleep(1)
    end = time.time()
    print("is_data Complete in {} seconds".format(end - start))


async def ins_data_1(li):
    start = time.time()
    for i in li:
        print(i)
        # await asyncio.sleep(0)
    end = time.time()
    print("is_data_1 Complete in {} seconds".format(end - start))


async def ins_main(li):
    start = time.time()
    await asyncio.wait([
        ins_data(li),
        ins_data_1(li)
    ])
    end = time.time()
    print("Complete in {} seconds".format(end - start))


if __name__ == '__main__':
    res = get_ins_data()
    print(res)
