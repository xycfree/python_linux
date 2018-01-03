#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/2/14 11:43
# @Descript:

import json
import requests

# 请求头部内容
# id,key
headers = {
    'X-LC-Id': 'YcgF9W1koVcijWTrISqQanV4-gzGzoHsz',
    'X-LC-Key': 'Xq07QEmn40vU4eiYqETcq9at',
    # 'Master_key': 'K9HpAwSNAkc7OSRiGW3pA2Kv',
    'Content-Type': 'application/json',
}
# 请求发送验证码 API
REQUEST_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/requestSmsCode'

# 请求校验验证码 API
VERIFY_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/verifySmsCode/'

def send_message(phone):
    '''通过POST请求requestSmsCode API发送验证码到指定手机
    :param phone: 手机号
    :return:
    '''
    data = {
        'MobilePhoneNumber': phone,
    }

    # post 方法参数包含三部分，如我们之前分析 API 所述
    # REQUEST_SMS_CODE_URL: 请求的 URL
    # data: 请求的内容，另外要将内容编码成 JSON 格式
    # headers: 请求的头部，包含 Id 与 Key 等信息
    r = requests.post(REQUEST_SMS_CODE_URL, data=json.dumps(data), headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False

def verify(phone, code):
    '''发送post请求到verifySmsCode API获取校验结果
    :param phone: 手机号
    :param code: 验证码
    :return:
    '''
    target_url = VERIFY_SMS_CODE_URL + "{code}?mobilePhoneNumber={phone}".format(code=code, phone=phone)
    r = requests.post(target_url, headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False
