#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-31 12:33:42
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import threading
import time, random
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
count = 0


def worker(n):
    print 'worker', n
    time.sleep(1)
    return


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))  #
        # t.setName('threads ...') #设置
        # print t.getName() #获取线程名称
        # t.setDaemon(True) #threading.setDaemon()的使用。设置后台进程
        threads.append(t)
        t.start()

        # 调用Thread.join将会使主调线程堵塞，直到被调用线程运行结束或超时。
        # 参数timeout是一个数值类型，表示超时时间，如果未提供该参数，
        # 那么主调线程将一直堵塞到被调线程结束
        # t.join(timeout=1)

    # threading.enumerate()的使用。此方法返回当前运行中的Thread对象列表
    for item in threading.enumerate():
        print 'thread list is ', item
    for item in threads:
        print item

        # print t.isAlive() #线程是否活着
        # print t.is_alive() #线程是否活着
print '当期进程的线程数为 {threads}'.format(threads=threading.activeCount() - 1)

print '*****************' * 5


class Mythread(threading.Thread):
    """docstring for Mythread"""

    def __init__(self, lock, thread_name):
        # 注意：一定要显式的调用父类的初始化函数。
        super(Mythread, self).__init__(name=thread_name)
        self.lock = lock

    def run(self):
        '''重写父类run方法，在线程启动后执行该方法内代码'''
        global count
        self.lock.acquire()  # 获取锁
        for i in range(10000):
            count += 1
        self.lock.release()  # 释放锁


lock = threading.Lock()  # 锁对象
for i in range(10):
    Mythread(lock, 'thread-' + str(i)).start()
print threading.activeCount() - 1
time.sleep(2)
print count

print '*****************' * 5


class Hider(threading.Thread):
    """捉迷藏的游戏，hider藏起来，通知seeker寻找"""

    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)
        self.cond.acquire()  # 产生一个锁
        print self.name + '我已经把眼睛蒙上了'
        self.cond.notify()  # 唤醒一个挂起的线程，notify()方法不会释放所占用的琐

        # wait方法释放内部所占用的琐，同时线程被挂起，直至接收到通知被唤醒或超时(如果提
        # 供了timeout参数的话）。当线程被唤醒并重新占有琐的时候，程序才会继续执行下去。
        self.cond.wait()  # wait方法释放内部所占用的琐，同时线程被挂起

        print self.name + '我找到你了'
        self.cond.notify()
        self.cond.release()

        print self.name + '我赢了'


class Seeker(threading.Thread):
    """docstring for Seeker"""

    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        self.cond.wait()

        print self.name + '我已经藏好了，你来找我吧'
        self.cond.notify()
        self.cond.wait()

        self.cond.release()
        print self.name + '被你找到了，哎'


cond = threading.Condition()  # 可以把Condiftion理解为一把高级的琐，它提供了比Lock, RLock更高级的功能，允许我们能够控制复杂的线程同步问题
seeker = Seeker(cond, 'seeker')
hider = Hider(cond, 'hider')
seeker.start()
hider.start()
