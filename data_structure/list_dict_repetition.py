#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/12/6 16:23
# @Author  : xycfree
# @Link    : http://example.org
# @Version : $
# @Descript: 

def list_dict_repetition(li):
    new_li = []
    lis = li
    for index, value in enumerate(li):
        value = value.get('title')
        print(value)
        if value not in new_li:
            new_li.append(value)
        else:
            del lis[index]
    print(new_li)
    return lis
li = [{'title':12},{'title':11},{'title':12},{'title':17},{'title':17}]
result = list_dict_repetition(li)
print(result)

#列表中的字典去重
resu = dict((x['title'],x) for x in li ).values()
print(resu)