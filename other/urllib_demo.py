#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-19 22:52:02
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import urllib
import re


def callback(a,b,c):
    down = 100.0 * a * b / c
    if down > 100:
        down = 100
    print '%.2f%%' % down,

print(dir(urllib))
print(help(urllib.urlopen))

#url = 'http://www.iplaypython.com/'
uuid = re.match('\w+\-\w+\-\w+-\w+-\w+','80fabe0b-6cc7-4648-8b82-68a101b70939').group()
print uuid
url = 'http://tr.psds.com.cn/web/report/'+ uuid + '.html'

html = urllib.urlopen(url)
#print html.read() #读取信息
#print html.read().decode('gbk','ignore').encode('utf-8')
print html.info() #返回头部信息
print html.getcode() #返回状态码
print html.geturl() #返回URL

#网页抓取，下载
urllib.urlretrieve(url,'.//u.html',callback) #callback方法显示下载进度
'''
传入网址，保存的路劲，一个函数的调用，可以定义函数的行为
但是需要保证函数有3个函数：
1.到目前为此传递的数据块数量
2.是每个数据块的大小，单位byte，字节
3.远程文件的大小。(有时候返回-1)

'''

html.close()


