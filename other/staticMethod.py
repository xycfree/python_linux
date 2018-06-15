#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-13 11:52:02
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import time
import sys
print sys.getdefaultencoding() #获取默认编码
reload(sys) #重新读取sys模块
sys.setdefaultencoding('utf8') #设置默认编码
class Date(object):
    """docstring for Date"""
    def __init__(self, year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year,t.tm_mon,t.tm_mday)

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year,t.tm_mon,t.tm_mday)
if __name__ == '__main__':
    a = Date(1977,4,12)
    print a.year,a.month,a.day
    b = Date.now()
    c = Date.tomorrow()
    print c

# @property 特殊装饰器应用
class Foo(object):
    """docstring for Foo"""
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise TypeError('must be a string')

        self.__name = value
    @name.deleter
    def name(self):
        raise TypeError('is not del')
f=Foo("wang")
n = f.name
print n
f.name = 'wang wang'
print f.name
#f.name = 233
#print f.name
#del f.name
#
#经验二：遇到字符（节）串，立刻转化为unicode，不要用str()，直接使用unicode()
unicode_str = unicode('中文', encoding='utf-8')
print unicode_str.encode('utf-8')
#经验三：如果对文件操作，打开文件的时候，最好用codecs.open，替代open(这个后面会讲到，先放在这里)
#import codecs
#codecs.open('filename', encoding='utf8')
