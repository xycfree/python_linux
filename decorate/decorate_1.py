#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/11/4 16:48
# @Author  : xycfree
# @Link    : http://example.org
# @Version : $

import os

#装饰器

def debug():
	import inspect
	call_name = inspect.stack()[1][3]
	print "['DEBUG']: enter {}() ".format(call_name)

def functions(func):
	def wrapper():
		print "[DEBUG]: enter {}()".format(func.__name__)
		print func()
		return func()
	print wrapper
	return wrapper

@functions
def start():
	#debug()
	print 'hello,start...'

def end():
	#debug()
	print 'hello,end...'




if __name__ == '__main__':
	start()
	#end()




