#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/4/20 18:59
# @Descript:
import json


def parse_text():
    with open('yingxiao360.txt', 'r') as f:
        text = f.read().splitlines()
        return text

result = parse_text()
print(type(result[0]))
print(result[0])
li = json.loads(result[0])
print(type(li))
print(len(li))
