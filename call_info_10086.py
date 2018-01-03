#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/13 16:09

import requests
from bs4 import BeautifulSoup

class CallInfo(object):
    def __init__(self):

        self.url = 'https://cmodsvr1.bj.chinamobile.com/PortalCMOD/detail/detail_all.jsp'
        self.url_1 = 'https://cmodsvr1.bj.chinamobile.com/PortalCMOD/detail/userdetailall.do'
        self.data = {
            'Month': '2017.01',
            # 'detailType': 'RC',
            'ssoSessionID': '2c9d82fb5968775c0159a4ef5c3e0f68',
            # 'sMobileType': '3',
            'detailType': 'GSM',
        }

        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=0000sU0eZ8XTIck7_jKHiOp-XCi:17oq08ouu',
            'Host': 'cmodsvr1.bj.chinamobile.com',
            'Referer': 'https://cmodsvr1.bj.chinamobile.com/PortalCMOD/InnerInterFaceBusiness?searchType=NowDetail&ssoSessionID=2c9d82fa596885b4015996ca98250e9b',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        }

    def get_call_info(self):
        session = requests.session()
        r = session.get(url=self.url_1, params=self.data, headers=self.headers)
        print(r.status_code)
        print(r.headers)
        print(r.cookies)
        print(r.url)
        print(r.text)

if __name__ == '__main__':
    call = CallInfo()
    result = call.get_call_info()