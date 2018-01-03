#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/8/11 9:57
# @Descript:


def yield_demo(max, *args, **kwargs):
    for i in max:
        yield i


if __name__ == '__main__':
    for i in yield_demo([1,2,3]):
        print(i)
    y = yield_demo([1,3,4,4,5,6,7,7,7,7,8])
    for i in y:
        print(i)