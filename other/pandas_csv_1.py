#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/11 9:32
from _csv import QUOTE_MINIMAL
from csv import Dialect

import pandas

class Excel(Dialect):
    delimiter = ''  # 单个字符，用于分隔字段
    quotechar = '"'  # 用于对特殊符号加引号，常见的引号为"
    doublequote = True  # 用于控制quotechar符号出现时的表现形式
    skipinitialspace = False  # 设置为True时delimiter后面的空格会被忽略
    lineterminator = '\r\n'  # 行结束符
    quoting = QUOTE_MINIMAL  # 是否在字段前加引号，quote_minimal表示仅当一个字段包含引号或定义符号时才加引号
    