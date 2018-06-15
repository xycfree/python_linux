#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/6/11 19:55
# Author: xycfree
# @Descript:  多线程  异步 队列, 获取的数据返回到主线程
import redis
import queue
import time
import threading
from threading import Thread

main_queue = queue.Queue(maxsize=1024)

def handle_callback(res):
    print("***当前线程: {}***".format(threading.current_thread().getName()))
    print(res)


class SetData:
    def __init__(self, key, value, handle=''):
        self.key = key
        self.value = value
        self.handle = handle


class AsyncRedisHandle(Thread):
    res = None
    _queue = queue.Queue(maxsize=1024)
    r = redis.Redis(host='172.16.0.224', port=6380, db=2)

    def send_set_cmd(self, key, value):
        set_data = SetData(key, value, handle=handle_callback)
        self._queue.put(set_data)

    def run(self):
        while True:
            while not self._queue.empty():
                item = self._queue.get()
                print('get item: {}, '.format(item))
                print("当前线程: {}".format(threading.current_thread().getName()))

                res = self.r.set(item.key, item.value)
                item.res = res
                main_queue.put(item)
                print("===当前线程: {}===".format(threading.current_thread().getName()))


                # item.handle(res)

            time.sleep(0.1)


if __name__ == '__main__':
    handle = AsyncRedisHandle()
    handle.start()
    handle.send_set_cmd('name', 'wang')
    while True:
        while not main_queue.empty():
            item = main_queue.get()
            item.handle(item.res)
        time.sleep(0.1)
    handle.join()
