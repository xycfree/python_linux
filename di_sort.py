#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/12/26 17:34

def results_sort(result):
    res = [[],[],[],[]] # 结果集
    types = ['news', 'weixin', 'zhihu', 'luntan']

    try:
        for i in result:
            print(i)
            print(type(i.get('type')))
            print(i.get('type'))
            index = 0
            index = types.index(i.get('type'))  # 获取字典的type值，查询type值得位置
            print(index)
            print(type(index))
            res[index].append(i)  # 字典追加到相应的列表里
            print(res[index])
        for i in range(len(res)):
            print res[i]

        res_list = []
        for i in range(len(res)):
            res_list += res[i]
        return res_list
    except Exception, e:
        raise e

result = [{'name':'wang11','type':'weixin'},{'name':'22','type':'news'},{'name':'wan','type':'zhihu'}]
print results_sort(result)
