#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xycfree
# @Date: 2018-06-19 17:38:41
# @Descipts:

import operator


def list_compare_info(li_old, li_new, cmps=False):
    """列表比较，cmps为True时表示比较所有"""
    temp = []

    if len(li_old) < len(li_new):
        _len = len(li_new) - len(li_old)
        print('_len: {}'.format(_len))
        temp = li_new[:_len]
        if not cmps:
            return temp
        else:
            for i in range(len(di_old)):
                res = dict_sort_info(li_old[i], li_new[i + _len])
                if res:
                    temp.append(dict(li_new[i + _len]))
            return temp
    elif len(li_old) == len(li_new):
        for i in range(len(li_old)):
                res = dict_sort_info(li_old[i], li_new[i])
                if res:
                    temp.append(dict(li_new[i]))
        return temp
        # if cmps:
        #     print('长度相等，比较字段')
        #     for i in range(len(li_old)):
        #         res = dict_sort_info(li_old[i], li_new[i])
        #         if res:
        #             temp.append(dict(li_new[i]))
        #     return temp
        # return False
    else:
        return False


def dict_sort_info(di_old, di_new):
    """字典进行比较"""
    print('di_old: {}'.format(di_old.get('id')))
    print('di_new: {}'.format(di_new.get('id')))
    try:
        print(di_old.pop('id', ''))
        print(di_new.pop('id', ''))
    except:
        print('id字段不存在')

    di_old_to_tuple = sorted(di_old.items(), key=lambda x: x[0], reverse=True)
    di_new_to_tuple = sorted(di_new.items(), key=lambda x: x[0], reverse=True)

    res = operator.eq(di_old_to_tuple, di_new_to_tuple)

    print('比较结果: {}'.format(res))
    return not res


if __name__ == '__main__':
    li = [
        {
            "id": 2563,
            "ent_id": "e2fe6312eb3db71a43eac3ff06696237",
            "entname": "小米科技有限责任公司",
            "hashCode": "92c6065b135ac69a5048ec277f56e381",
            "keyword_id": 392,
            "news_date": "2018-06-14 15:01:29",
            "news_title": "5G标准按时完成,产业携手加速商用步伐",
            "news_summary": "联发科技、倢通科技股份有限公司、三菱电机、日本电气...Verizon、VIAVI、vivo、沃达丰、小米、中兴等公司联合...来源:中国移动研究院责任编辑:马利亚2018世界VR...",
            "keyword": "小米科技有限责任公司",
            "news_source": "电子信息产业网",
            "source_url": "",
            "news_url": "http://cyyw.cena.com.cn/2018-06/14/content_389670.htm",
            "page_view_count": "",
            "emotion_value": "",
            "review_count": "",
            "praise_count": "",
            "publish": "",
            "category": "新闻",
            "create_date": "2018-06-14 15:03:29",
            "update_date": ""
        },
        {
            "id": 2571,
            "ent_id": "e2fe6312eb3db71a43eac3ff06696237",
            "entname": "小米科技有限责任公司",
            "hashCode": "5b57575ab0f47b0cafcb7d08b3eb128b",
            "keyword_id": 392,
            "news_date": "2018-06-14 15:00:29",
            "news_title": "湘妍健被评为中国健康产业十大创新品牌",
            "news_summary": "“2018(第二届)中国经济峰会”于5月11日至13日在北京拉开帷幕。湖南中沙中医科技有限公司湘妍健品牌被评为中国健康产业十大创新品牌。",
            "keyword": "小米科技有限责任公司",
            "news_source": "中华网财经",
            "source_url": "",
            "news_url": "http://finance.china.com/hyzx/20000618/20180614/25224382.html",
            "page_view_count": "",
            "emotion_value": "",
            "review_count": "",
            "praise_count": "",
            "publish": "",
            "category": "新闻",
            "create_date": "2018-06-14 15:03:29",
            "update_date": ""
        }
    ]

    li2 = [
        {
            "id": 2569,
            "ent_id": "e2fe6312eb3db71a43eac3ff06696237",
            "entname": "小米科技有限责任公司",
            "hashCode": "92c6065b135ac69a5048ec277f56e381",
            "keyword_id": 392,
            "news_date": "2018-06-14 15:01:29",
            "news_title": "5G标准按时完成,产业携手加速商用步伐",
            "news_summary": "联发科技、倢通科技股份有限公司、三菱电机、日本电气...Verizon、VIAVI、vivo、沃达丰、小米、中兴等公司联合...来源:中国移动研究院责任编辑:马利亚2018世界VR...",
            "keyword": "小米科技有限责任公司",
            "news_source": "电子信息产业网",
            "source_url": "",
            "news_url": "http://cyyw.cena.com.cn/2018-06/14/content_389670.htm",
            "page_view_count": "",
            "emotion_value": "",
            "review_count": "",
            "praise_count": "",
            "publish": "",
            "category": "新闻",
            "create_date": "2018-06-14 15:03:29",
            "update_date": ""
        },
        {
            "id": 2571,
            "ent_id": "e2fe6312eb3db71a43eac3ff06696237",
            "entname": "小米科技有限责任公司",
            "hashCode": "5b57575ab0f47b0cafcb7d08b3eb128b",
            "keyword_id": 392,
            "news_date": "2018-06-14 15:00:29",
            "news_title": "湘妍健被评为中国健康产业十大创新品牌",
            "news_summary": "“2018(第二届)中国经济峰会”于5月11日至13日在北京拉开帷幕。湖南中沙中医科技有限公司湘妍健品牌被评为中国健康产业十大创新品牌。",
            "keyword": "小米科技有限责任公司",
            "news_source": "中华网财经",
            "source_url": "",
            "news_url": "http://finance.china.com/hyzx/20000618/20180614/25224382.html",
            "page_view_count": "",
            "emotion_value": "",
            "review_count": "",
            "praise_count": "",
            "publish": "",
            "category": "新闻",
            "create_date": "2018-06-14 15:03:29",
            "update_date": ""
        }
    ]
    res = list_compare_info(li, li2)
    print(res)
