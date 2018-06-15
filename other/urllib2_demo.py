#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-20 22:41:18
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import urllib2

url = 'http://blog.csdn.net/u013088062/article/details/49705439'

#添加头部请求信息
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "Host" : "blog.csdn.net",
    "Referer" : "http://blog.csdn.net/column/details/pythonplane.html",
    "GET" : url
}
#req.add_header("GET",url)
req = urllib2.Request(url,headers=headers)

content = urllib2.urlopen(req)
print content.read()
print content.info()
