#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-21 16:17:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import pickle
import shelve

'''
对象持久化pickle
    dump() 将对象写入文件
    load() 对象还原
    shelve模块类似pickle，shelve将对象保存在一个类似字典的数据库中
    
'''
obj = '{"name":"zwhset","age":14}'
def obj_dump(f):

    f = open(f,'wb') #二进制写
    pickle.dump(obj,f)
    pickle.dump(obj,f,2) #使用协议2保存
    pickle.dump(obj,f,pickle.HIGHEST_PROTOCOL) #使用最先进的协议
    f.close()

def obj_load(f):
    f = open(f,'rb')
    obj = pickle.load(f)
    print 'obj:{0}'.format(obj)
    f.close()

def obj_shelve(f):
    db = shelve.open(f) #open is shelve
    db['key'] = obj #object save is shelve

    obj = db['key'] #search(retrieve) object 检索对象
    db.close()


if __name__ == '__main__':
    f = 'obj.txt'
    obj_dump(f)
    obj_load(f)
