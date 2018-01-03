#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/6/23 17:53
# @Descript:
import json

import requests

"""http://mp.weixin.qq.com/s
?__biz=MjM5NDA5OTAwMg==
&mid=2651692978&idx=4
&sn=8de12474f841943ce16fb73f9ec1a239
&chksm=bd75c5e78a024cf1dfef4c2bb4df537a6a31bfb599e90319fb850e17436b9de178e5036ec852
&mpshare=1
&scene=1
&srcid=0808FmGWBHfrVIDkI82gOrcr#rd"""
def vote():
    data = {
        'aid': '337',
        'apply_id': '15474',
        'third_app_token': '',
    }
    headers = {
        'Host': 'zjk031303.com',
        'Connection': 'keep-alive',
        'Content-Length': '31',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://zjk031303.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.556.400 QQBrowser/9.0.2524.400',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://zjk031303.com/vote_new/web/wap/default/list/?aid=337&type=all',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
        'Cookie': 'PHPSESSID=t4177s1embgcs1f8dsbvt281u7; foobaropenid=oUcVes-ef1yfyICZnlJT8NRrXJ70; foobaruid=417181',
    }
    sess = requests.Session()
    response = sess.post('http://zjk031303.com/vote_new/web/wap/default/vote', data=data, headers=headers)
    if response.status_code != 200:
        print('交易失败')
        print('返回状态：{}'.format(response.status_code))
        print(json.loads(response.content.decode('utf-8')))
    else:
        print('返回状态：{}'.format(response.status_code))
        print(json.loads(response.content.decode('utf-8')))



if __name__ == '__main__':
    vote()
