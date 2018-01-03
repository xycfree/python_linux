#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/9 15:51
import re
import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.content, 'lxml')
for child in bsObj.find("table", {"id":"giftList"}).children:  # 查找子标签 .children
    print(child)
print('#####'*5)

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:  # 处理兄弟标签
    # BeautifulSoup的next_siblings()函数可以让收集表格数据成为简单的事情，尤其是处理带标题行的表格
    print(sibling)

    '''
    这段代码会打印产品列表里的所有行的产品，第一行表格标题除外。为什么标题行被跳过了呢？有两个理由。首先，对象不能把自己作为兄弟标
    签。任何时候你获取一个标签的兄弟标签，都不会包含这个标签本身。其次，这个函数只调用后面的兄弟标签。例如，如果我们选择一组标签中位
    于中间位置的一个标签，然后用 next_siblings() 函数，那么它就只会返回在它后面的兄弟标签。因此，选择标签行然后调用 next_siblings，可以选
    择表格中除了标题行以外的所有行。
    '''

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
# 父标签parent，previous_sibling上一个兄弟标签

html = requests.get("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html.content,'lxml')
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                      href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])