#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/16 18:34

# 验证码识别，此程序只能识别数据验证码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from PIL import Image, ImageEnhance, ImageFilter
from pytesser import *

# 二值化
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

# 由于都是数字
# 对于识别成字母的 采用该表进行修正
rep = {'O': '0', 'Q': '0',
       'I': '1', 'L': '1',
       'Z': '2',
       'S': '8'
       };


def getverify1(name):
    # 打开图片
    im = Image.open(name)
    # 转化到灰度图
    imgry = im.convert('L')
    # 保存图像
    imgry.save('g' + name)
    # 二值化，采用阈值分割法，threshold为分割点
    out = imgry.point(table, '1')
    out.save('b' + name)
    # 识别
    text = image_to_string(out)
    # 识别对吗
    text = text.strip()
    text = text.upper()
    for r in rep:
        text = text.replace(r, rep[r])
        # out.save(text+'.jpg')
    print text
    return text

result = getverify1('1.jpg')  # 注意这里的图片要和此文件在同一个目录，要不就传绝对路径也行
print(eval(result[:3]))
