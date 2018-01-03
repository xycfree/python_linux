#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/4/10 19:08
# @Descript: jieba分词

import jieba

seg_list = jieba.cut("品尚电子商务有限公司",cut_all=True)
print("全匹配:", "/ ".join(seg_list))

seg_list = jieba.cut("品尚电子商务有限公司",cut_all=False)
print("精确匹配:", "/ ".join(seg_list))

seg_list = jieba.cut("品尚电子商务有限公司") #默认是精确模式
print('默认匹配:', ", ".join(seg_list))

seg_list = jieba.cut_for_search("品尚电子商务有限公司") #搜索引擎模式
print('搜索引擎模式匹配:', ", ".join(seg_list))
