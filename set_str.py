#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/3/28 15:35
# @Descript:
import json
import re

str = """{"data":["调高,2017/3/22 10:59:11,APPHiCl79rUuIndustry,10001005,东北证券,3,475,持有,优于大势,看懂银行系列报告之一："央行宏观审慎评估体系"（MPA）全解析,银行,0.47",
    "维持,2017/3/22 21:54:08,APPHiD16e4n9Industry,80000134,华金证券,1,475,持有,领先大市,银行行业深度分析：桎梏渐消&sbquo;掘金银行,银行,0.47",
    "无,2017/3/21 10:10:38,APPHiCl72AjnIndustry,80000075,申万宏源,4,475,持有,看好,银行业周报：公开市场操作利率上行10BP&sbquo;继续推荐银行板块,银行,0.47","无,2017/3/21 14:49:03,APPHiCl74xbpIndustry,80403294,IBM商业价值研究院,,475,,,智慧的银行业,银行,0.47",
    "无,2017/3/21 14:52:12,APPHiCl74xbyIndustry,80001777,毕马威,,475,,,中国银行业上市银行业绩回顾及热点问题探讨,银行,0.47","维持,2017/3/20 11:14:12,APPHiCX7bJ9RIndustry,80000037,平安证券,4,475,持有,强于大市,银行行业周报：央行上调资金利率&sbquo;多地加码房地产限购政策,银行,0.47",
    "维持,2017/3/20 13:46:37,APPHiCX7bNRRIndustry,10000082,国金证券,5,475,买入,买入,银行业行业周报：板块下调幅度收窄；进入年报披露期,银行,0.47",
    "无,2017/3/20 13:55:58,APPHiCI8FuiwIndustry,80000075,申万宏源,4,475,持有,看好,银行：再论&quot;驱动力信号验证&quot;策略体系报告之五："银行投资的策略思维",银行,0.47",
    "维持,2017/3/20 14:12:14,APPHiCX7bskRIndustry,10001075,广发证券,4,475,买入,买入,银行业周报：逆回购和MLF中标利率再次上行&sbquo;不改行业基本面趋势,银行,0.47",
    "维持,2017/3/15 7:53:07,APPHiB7AnjFaIndustry,80000134,华金证券,1,475,持有,领先大市,银行行业动态分析：表外社融压缩显著&sbquo;M2增速回落,银行,0.47",
    "维持,2017/3/15 8:03:56,APPHiB7ApE21Industry,80000140,财富证券,2,475,持有,谨慎推荐,银行业3月点评报告：又到融资季,银行,0.47",
    "pages":"49","update":"2017-03-24","count":"1203"}"""

def str_json(content):
    """非规则json数据，进行格式化"""
    for x in re.findall(r'("\W+")', content):  # 匹配任意非数字和字母的字符，相当于 [^a-zA-Z0-9_]
        if not set(x) & set([',', ']', '[', '{', '}', '(', ')', ':']):  # 集合交集，为空则替换
            p = re.findall(r'"(\W+)"', x)
            print('P: {}'.format(json.dumps(p, ensure_ascii=False)))
            if p:
                ret = p[0]
                print('res is : {}'.format(ret))
                content = re.sub(x, ret, content)
            else:
                content = re.sub(x, '', content)
    return content

result = str_json(str)
print(result)