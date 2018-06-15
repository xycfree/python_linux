#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-12 12:56:43
# @Author  : xycfree@163.com
# @Link    : http://example.org
# @Version : $Id$

import os
import sys

dirroot = r"d:\pyworkspace\gitcoding\python_linux"
line_num = 0
li = []
# parent是父文件夹 dirnames是dirroot含的文件夹 filenames是所有文件
for parent, dirnames, filenames in os.walk(dirroot):

    print('进入文件夹：', dirroot)
    for dirname in dirnames:
        # print 'parent is ', parent
        print('文件夹  ', dirname)

    for filename in tuple(filenames):
        # print "parent is " + parent
        print("文件 " + filename)
        # print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息

    li.append(os.path.join(parent, filename))
    for l in tuple(li):
        print("所有文件路径信息：", l)
