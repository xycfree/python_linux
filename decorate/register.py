#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/3/31 16:29
# @Descript: 注册装饰器
import functools
from Queue import Queue

_functions = {}
def register(f):
    global _functions
    _functions[f.__name__] = f
    print(_functions)
    return f

@register
def foo():
    return 'bar'


def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            print('username:{} is not admin'.format(kwargs.get('username')))
            # raise Exception("This user is not allowed to get food!")
        return f(*args, **kwargs)
    return wrapper

class Store(object):
    def __init__(self):
        self.storage = Queue(maxsize=100)

    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        self.storage.put(food)

if __name__ == '__main__':
    s = Store()
    res = s.put_food(username='admin1', food='haha')
    print(res)

    res = s.get_food(username='admin1', food='haha')
    print(res)