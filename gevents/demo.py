#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/7/24 11:01
# Author: xycfree
# @Descript:

from lxml import etree
import aiohttp
import asyncio
import async_timeout

async def fetch(url):
    print('start...')
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    try:
        async with aiohttp.ClientSession() as session:
            with async_timeout.timeout(10):
                async with session.get(url, headers=head) as response:
                    if response.status != 200:
                        print('请求失败, status: {}, text: {}'.format(response.status, await response.text()))
                        return None
                    _text = await response.text()
                    soup = etree.HTML(_text)
                    divs = soup.xpath(".//*[@class='result']")
                    print("divs is len: {}".format(len(divs)))
                    ss = [i.xpath("div/p/text()") for i in divs]
                    print(ss)
                    return ss
    except Exception as e:
        print(e)
        return None

if __name__ == '__main__':
    print('xxxxxxxxxxxxxxxxxxxxxxxxxx')
    url = "http://news.baidu.com/ns?d1=24&bt=0&begin_date=2018-07-24&q4=&y1=2018&lm=8640&d0=24&ct1=0&et=0&mt=8640&ie=utf-8&from=news&ct=0&q1=浙江阿里巴巴电子商务有限公司&end_date=2018-07-24&m1=07&clk=ortbytime&pn=0&m0=07&cl=2&rn=50&q6=&s=1&tn=newsdy&q3=&submit=百度一下"
    url1 = "http://news.baidu.com/ns?d1=24&bt=0&begin_date=2018-07-24&q4=&y1=2018&lm=8640&d0=24&ct1=0&et=0&mt=8640&ie=utf-8&from=news&ct=0&q1=浙江阿里巴巴电子商务有限公司&y0=2018&end_date=2018-07-24&m1=07&clk=ortbytime&pn=0&m0=07&cl=2&rn=50&q6=&s=1&tn=newsdy&q3=&submit=百度一下"
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(fetch(url1))
    print(res)
