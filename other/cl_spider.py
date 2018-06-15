#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/13 9:29

import os
import re
import urllib
import requests
from __builtin__ import raw_input

from lxml import etree
from bs4 import BeautifulSoup

"""
[url]http://www.guodilao.com/thread0806.php?fid=16&search=&page=1[/url]
[url]http://www.guodilao.com/thread0806.php?fid=16&search=&page=2[/url]
"""
"""
图片
"""


class Spider:
    def __init__(self):
        print("Happy-V1.0")
        self.startPage = int(raw_input("请输入起始页："))
        self.endPage = int(raw_input("请输入终止页："))
        self.url = "http://www.guodilao.com/thread0806.php?fid=16&search=&page="
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    def spiderWork(self):
        for each in range(self.startPage, self.endPage + 1):
            url = self.url + str(each)
            # print url
            self.loadPage(url)

    def loadPage(self, link):
        request = requests.get(link, headers=self.headers)
        html = request.text
        xmlMsg = etree.HTML(html)
        # print xmlMsg
        urlList = xmlMsg.xpath('*//div[@class="t"]/table/tbody[2]/tr/td[2]/h3/a/@href')
        # print urlList
        # 创建保存目录
        souceFileName = "./Images/"
        # 如果目录不存在，则创建目录
        if (not os.path.exists(souceFileName)):
            os.makedirs(souceFileName)
        for i, everyUrl in enumerate(urlList):
            # print everyUrl
            if re.match(r'read.php.*', everyUrl):
                pass
            else:
                everyUrl = "http://www.guodilao.com/" + everyUrl
                # print i,everyUrl
                self.downloadPic(everyUrl, i + 1, souceFileName)

    def downloadPic(self, pageUrl, num, path):
        request = requests.get(pageUrl, headers=self.headers)
        htmlMsg = request.text
        xmlMsg = etree.HTML(htmlMsg)
        imagesLinks = xmlMsg.xpath('*//div[@class="tpc_content do_not_catch"]/input/@src')
        # 图片后缀
        for imgId, imgUrl in enumerate(imagesLinks):
            # print imgUrl
            # 拿到图片的名字
            baseName = os.path.basename(imgUrl)
            # 拿到图片的后缀
            last = os.path.splitext(baseName)[1][1:]
            # print last
            print("正在存储文件 ----->>", str(num) + '-' + str(imgId + 1) + '.' + last)

            filename = path + '/' + str(num) + '-' + "%d.jpg" % (imgId + 1)

            req = requests.get(imgUrl, headers=self.headers)
            imgData = req.content.decode('utf-8')
            with open(filename, 'wb') as file:
                file.write(imgData)
            file.close()


if __name__ == "__main__":
    spider = Spider()
    spider.spiderWork()