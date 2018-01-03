#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/16 17:25

# !/usr/bin/python
# encoding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from lxml import etree
import time, datetime
import re
from switch import *
from PIL import Image
import sys
import pyocr
import pyocr.builders
import pytesseract

image_path = 'verify1.jpg'

im = Image.open(image_path)
imgry = im.convert('L')
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
out.show()
# 读取出字符串
cap_str = pytesseract.image_to_string(out)
print cap_str


