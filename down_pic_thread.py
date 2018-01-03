#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-01 22:26:01
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import sys
import threading
from multiprocessing.dummy import Pool

import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

pic_path = 'pic/'  # 保存文件路径

URL = 'http://www.nanrenwo.net/z/tupian/hashiqitupian/'
URL1 = 'http://www.nanrenwo.net/'


class Worker(threading.Thread):
    def __init__(self, url, img, filename):
        super(Worker, self).__init__()
        self.url = url
        self.img = img
        self.filename = filename

    def run(self):
        try:
            u = self.url + self.img
            r = requests.get(u, stream=True)
            with open(self.filename, 'wb') as fd:
                for chunk in r.iter_content(4096):
                    fd.write(chunk)
        except Exception as e:
            raise e


def get_imgs(url):
    t = 1
    r = requests.get(url, stream=True)
    soup = BeautifulSoup(r.text, 'lxml')
    myimg = [img.get('src') for img in soup.find(id='brand-waterfall').find_all('img')]  # 查询id下所有img元素
    print('myimg:', myimg)
    for img in myimg:
        pic_name = pic_path + str(t) + '.jpg'
        # img_src = img.get('src')
        print('img: ', img)
        # self.download_pic(URL1,img,pic_name) #request Url,img src,picture name
        w = Worker(URL1, img, pic_name)
        w.start()
        t += 1


def get_imgs_thread_pool(url):
    """线程池方式实现"""
    t = 1
    r = requests.get(url, stream=True)
    soup = BeautifulSoup(r.text, 'lxml')
    myimg = [img.get('src') for img in soup.find(id='brand-waterfall').find_all('img')]  # 查询id下所有img元素
    # print('myimg:', myimg)
    pool = Pool(100)  # 申请100个线程

    pool.map(get_image_save, myimg)
    pool.close()
    pool.join()


def get_image_save(myimg):
    print(myimg)
    pic_name = pic_path + str(myimg.rsplit('/', 1)[1])  # + '.jpg'
    get_image_down(myimg, pic_name)


def get_image_down(myimg,pic_name):
    try:
        u = URL1 + myimg
        r = requests.get(u, stream=True)
        with open(pic_name, 'wb') as fd:
            for chunk in r.iter_content(4096):
                fd.write(chunk)
        print('download success..')
    except Exception as e:
        raise e

# get_imgs(URL)
get_imgs_thread_pool(URL)
