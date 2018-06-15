#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/11/28 15:03
# @Author  : xycfree
# @Link    : http://example.org
# @Version : $

import os
import threading

mutex_lock = threading._RLock()  # 互斥锁申明
ticket = 100000  # 总票数
t_thread1 = 0
t_thread2 = 0
t_thread3 = 0
t_thread4 = 0
t_thread5 = 0


class Mythread(threading.Thread):
    """多线程抢票"""

    def __init__(self, name):
        super(Mythread, self).__init__()  # 线程类必须要初始化
        self.thread_name = name

    def run(self):
        # 申明在类中使用全局变量
        global mutex_lock
        global ticket
        global t_thread1, t_thread2, t_thread3, t_thread4, t_thread5

        while True:
            mutex_lock.acquire()  # 临界区开始，互斥开始
            # 仅能有一个线程
            if ticket > 0:
                ticket -= 1
                # 统计那个线程拿到票
                print('{0}抢到了票，还剩{1}张'.format(self.thread_name, ticket))

                if self.thread_name == '线程1':
                    t_thread1 += 1
                elif self.thread_name == '线程2':
                    t_thread2 += 1
                elif self.thread_name == '线程3':
                    t_thread3 += 1
                elif self.thread_name == '线程4':
                    t_thread4 += 1
                elif self.thread_name == '线程5':
                    t_thread5 += 1
            else:
                break
            mutex_lock.release()  # 临界区结束，互斥结束，释放锁
        mutex_lock.release()  # python在线程死亡时，不会清理一存在线程函数的互斥锁，必须手动主动清理
        print('{}被销毁了'.format(self.thread_name))


print('start...')
threads = []
for i in range(1, 6):
    threads.append(Mythread('线程' + str(i)))
for t in threads:
    t.start()
for t in threads:
    t.join()

print('票都被抢光了！！！')
for i in range(1, 6):
    print('线程{0}:{1}'.format(str(i), eval('t_thread' + str(i))))
