#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-27 14:50:52
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
class Person(object):
    def __init__(self):
        print('父类init ...')

    def eat(self):
        print('Person pepole eat...')


class Sub(Person):
    """docstring for Sub"""
    def __init__(self):
        Person.__init__(self)
        print('子类 init ...')

    def eat(self):
        super(Sub,self).eat()
        print('Sub pepole eat...')

    def eating(self):
        Person.eat(self)
        print('i not eating...')


p=Person()
p.eat()

c=Sub()
c.eat()
c.eating()
        
