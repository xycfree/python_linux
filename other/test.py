#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-02 16:15:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import threading
import time

loops = [4,2]

class ThreadFunc(object):

    def __init__(self,func,args,name=''):
        self.func = func
        self.args = args
        self.name = name
    def __call__(self):
        apply(self.func,self.args)

def loop(nloop,nsec):
    print 'start loop ',nloop,'at: ',time.ctime()
    time.sleep(nsec)
    print 'start loop ',nloop,'at: ',time.ctime()

def main():
    print 'start at:',time.ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
       
        #t = threading.Thread(target=loop,args=(i,loops[i]))
        t = threading.Thread(target=ThreadFunc(loop,(i,loop[i]),loop.__name__))
        threads.append(t)
    for i in nloops:
       
        threads[i].start()
    for i in nloops:
       
        threads[i].join()

    print 'all done at:',time.ctime()
if __name__ == '__main__':
    main()
