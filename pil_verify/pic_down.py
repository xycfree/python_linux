#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/17 17:08
import requests
u = 'http://cpquery.sipo.gov.cn/freeze.main?txn-code=createImgServlet&freshStept=1&now=Tue%20Jan%2017%202017%2016:59:24%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)'
r = requests.get(u, stream=True)
chunk_size = 4096  # 写入图片大小
with open('aa.jpg', 'wb') as fd:
    for chunk in r.iter_content(chunk_size):
        fd.write(chunk)

