#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/23 15:25
# @Descript: 

import requests
from bs4 import BeautifulSoup

login_url = 'https://www.itjuzi.com/user/login'
headers_ = {
            'Host': 'www.itjuzi.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.itjuzi.com/user/login',
            # 'Cookie': 'acw_tc=AQAAAO+AIjnBIgUAPXbQcVbhXwSnwAGt; gr_session_id_eee5a46c52000d401f969f4535bdaa78=d45f17dc-10ab-4883-bd6b-d63abc89d8fe; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1485136988; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1485136988; gr_user_id=87ee6f1e-058c-49f5-a54d-d2d31af49bfb; _ga=GA1.2.1461322093.1485136989; session=7f4f909b6c25cb8b5243a1ef811f8c46b1f416fd; _gat=1',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '65',
        }
formdata = {'identity': 'zjkkbne@163.com',
            'password': 'zjkkbne',
            'remember': '1',
            'page': '',
            'url': '',
            }
session = requests.session()
r = session.post(login_url, data=formdata, headers=headers_, verify=False)
print(r.status_code)
print(r.headers)
soup = BeautifulSoup(r.content, 'lxml')
page=1
comp = session.get('http://www.itjuzi.com/company',headers=r.headers).content
soup = BeautifulSoup(comp, 'lxml')
print(soup)
