#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-19 16:09:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import random
import base64
import hashlib

#密码字符串池
pwdStrPool = '0123456789abcdefghijkmnpqrstuvwxyz~@#$%^&*()_+'\
    'ABCDEFGHIJKMNPQRSTUVWXYZ'
#密码字符串池长度
pwdStrPoolSize = len(pwdStrPool)
#定义要生成的密码长度
pwdLen = [16,16]

#获取一个固定长度的随机串
def get_randNum(p):
    randStr = ''
    for i in range(p):
        randNum = random.randint(0,pwdStrPoolSize-1)
        randStr += pwdStrPool[randNum]
    return randStr
#base64加密
def base64_encode(strs):
    str_encode = base64.encodestring(strs)
    return str_encode

#base64解密
def base64_decode(strs):
    str_decode = base64.decodestring(strs)
    return str_decode

#MD5加密
def md5(strs):
    #import hashlib
    m = hashlib.md5() #创建md5对象
    m.update(strs) #生成机密串
    pwd = m.hexdigest() #获取加密串
    return pwd


def tester():
    print get_randNum(random.randint(pwdLen[0],pwdLen[1]))

if __name__ == '__main__':
    strs = get_randNum(random.randint(0,pwdLen[0]))
    print 'strs: %s' %strs
    print 'base64加密后：%s' %base64_encode(strs)
    print 'md5加密后：%s' % md5(strs)
