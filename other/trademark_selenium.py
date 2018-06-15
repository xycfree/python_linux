#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/10/31 10:18
# @Descript:
import time
from lxml.html import etree

import requests
from selenium import webdriver

base_url = "http://www.sbcx.com"

def trade(url):
    _path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    phantomjs_path = r"D:\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe"  # "D:\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe"
    driver = webdriver.Chrome(_path)
    # driver = webdriver.PhantomJS(executable_path=phantomjs_path)
    driver.get(url)
    print(driver.get_cookies())
    print(driver.title)
    driver.implicitly_wait(3)
    driver.maximize_window()
    cookies = driver.get_cookies()
    _text = driver.find_elements_by_xpath('//*[@id="icons"]/table/tbody/tr')
    print(len(_text))
    li = []
    for i in _text[1:25]:
        try:
            info = {}
            info['icon'] = i.find_element_by_xpath("td[1]/a/img").get_attribute("src")
            info['name'] = i.find_element_by_xpath("td[2]/a").text
            detail = i.find_element_by_xpath("td[2]/a").get_attribute("onclick").split("('")[1].split("'")[0]
            info['detail_url'] = base_url + detail
            info['category'] = i.find_element_by_xpath("td[3]/a").text
            info['status'] = i.find_element_by_xpath("td[4]/a").text
            info['register'] = i.find_element_by_xpath("td[5]/a").text
            info['proposer'] = i.find_element_by_xpath("td[6]/a/font").text
            info['date'] = i.find_element_by_xpath("td[7]/a").text
            info['content'] = get_content_info(info['detail_url'])
            print(info)
            li.append(info)
        except Exception as e:
            print(e)
    return li


def get_content_info(url):
    time.sleep(0.5)
    sess = requests.session()
    r = sess.get(url)
    if r.status_code != 200:
        return {}
    try:
        _text = r.content.decode('utf-8')
        sel = etree.HTML(_text)
        _keys = sel.xpath(".//*[@class='xxnrxq_left']/text()")
        _values = sel.xpath(".//*[@class='xxnrxq_left01']/text()")
        info = dict(zip(_keys, _values))
        return info
    except Exception as e:
        print(e)
        return {}



if __name__ == '__main__':
    entname = "小米科技有限责任公司"
    url = "http://www.sbcx.com/sbcx/" + entname
    res = trade(url)
    print(res)