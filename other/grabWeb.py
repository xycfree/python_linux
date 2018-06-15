#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-25 15:13:10
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from urllib import urlretrieve
#输出问文件的第一行和最后一行
def first_non_blank(lines):
    for eachline in lines:
        if not eachline.strip():
            continue
        else:
            return eachline

def first_last(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print first_non_blank(lines)
    lines.reverse()
    print first_non_blank(lines)

def download(url='http://tr.psds.com.cn/web/nindex.html',process = first_last):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:
        process(retval)
if __name__ == '__main__':
    download()
    