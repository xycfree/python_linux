#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xycfree
# @Date: 2018-06-15 14:38:57
# @Descipts: gevent具有确定性, 在配置相同的输入情况下，会产生相同的输出；

import time


def echo(i):
    time.sleep(0.01)
    return i


if __name__ == '__main__':
    from multiprocessing.pool import Pool

    p = Pool(10)
    run1 = [i for i in p.imap_unordered(echo, range(10))]
    run2 = [i for i in p.imap_unordered(echo, range(10))]
    run3 = [i for i in p.imap_unordered(echo, range(10))]
    print(run1 == run2 == run3)
    print(run1)
    print(run2)
    print(run3)


    from gevent.pool import Pool

    p = Pool(10)
    run1 = [i for i in p.imap_unordered(echo, range(10))]
    run2 = [i for i in p.imap_unordered(echo, range(10))]
    run3 = [i for i in p.imap_unordered(echo, range(10))]
    print(run1 == run2 == run3)
    print(run1)
    print(run2)
    print(run3)
