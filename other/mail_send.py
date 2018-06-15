#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-30 14:06:18
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$



import os
import smtplib
import string

#邮件发送服务
FROM = 'bingpoli@163.com'    #raw_input("请输入您的邮箱地址：")
FROM_PASS = raw_input("请输入邮箱密码：")
HOST = 'smtp.163.com'     #raw_input("请输入邮箱服务器地址：") #smtp.163.com
TO = raw_input('对方邮箱：')
SUBJECT = "Mail"
text = 'this is test mail!'
BODY = string.join(('FROM: %s' % FROM,
                    'TO: %s' % TO,
                    'Subject: %s' % SUBJECT,
                    "",
                    text),'\r\n')
server = smtplib.SMTP()
server.connect(HOST,'25')
server.login(FROM,FROM_PASS)
server.sendmail(FROM,[TO],BODY)
server.quit()
