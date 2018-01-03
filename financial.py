#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-06 16:51:18
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import MySQLdb
import time
import re
import db_mysql
from decimal import *
import math

class Financial(object):

    def __init__(self, cu_no,create_time):
        self.cu_no = cu_no
        self.create_time = create_time
        self.db_object = db_mysql.db_object()
        self.conn = self.db_object[0]
        self.cur = self.db_object[1]



    def express_resolve(self, name):
        '''
            通过name解析express表达式
        '''
        self.query = 'SELECT express FROM cr_report_item_config WHERE name LIKE "%{name}%"'.format(name=name)
        self.express = db_mysql.db_select_on(self.query)  # 表达式
        print self.express[0]   # 输出表达式

        self.exprs = re.findall(r'[a-zA-Z]{2}\d{1}', self.express[0])  # 表达式指标表
        self.exprs1 = re.findall(r"\'\d{3,4}\'",self.express[0])  #指标项
        print self.exprs
        print self.exprs1
        li = []
        for j,i in enumerate(self.exprs):
            self.tab,self.years = self.ret_table(i) #获取表名和年度
            print self.tab,self.years
            self.index_terms = self.exprs1[j][1:-1]  #获取指标项line_num
            print self.index_terms
            #查询数据库数据，substring(report_date,1,4)截取日期中的年
            #SELECT * FROM `cr_core_income_statement` WHERE SUBSTRING(report_date,1,4) = '2016'
            self.query1 = 'SELECT item_sum FROM {table} WHERE cu_no="{cu_no}" AND\
            line_num="{line_num}" AND SUBSTRING(report_date,1,4)="{date}" and SUBSTRING(createTime,1,10)="{create_time}"'.format(\
                table=self.tab,cu_no=self.cu_no,line_num=self.index_terms,date=self.years,create_time=self.create_time)
            #print self.query1
            self.resu = db_mysql.db_select_on(self.query1) #获取数据值item_sum 返回元组
            li.append(self.resu)

        print li
        s = re.sub(r"\w+\[\'\d+\'\]",'?',self.express[0])
        exp = self.replace_exp(s,li).lower()
        print exp , eval(exp)



    def replace_exp(self,s,li):
        '''
            表达式中的指标项替换为数据库查询的数据
         '''
        self.m = ''
        for i in li:
            if self.m == '':
                self.s = s.replace('?',str(i[0]),1)
                self.m = self.s
            else:
                self.m = self.m.replace('?',str(i[0]),1)
        return self.m

    def ret_table(self, expr):
        '''
            根据表达式指标表返回数据表和年度表数据
         '''
        self.ta = expr[:2]
        self.years = expr[2:]
        if self.ta == 'zf':
            self.ta1 = 'cr_core_balance_sheet' #资产负债表
        elif self.ta == 'xl':
            self.ta1 = 'cr_core_cashflow_statement' #现金流量表
        else:
            self.ta1 = 'cr_core_income_statement' #损益表

        if self.years == '1':
            self.years1 = '2016'
        elif self.years == '2':
            self.years1 = '2015'
        else:
            self.years1 = '2014'
        return self.ta1, self.years1

if __name__ == '__main__':
    name = '净利润增长率(单位：%)'
    create_time = '2016-09-08'
    fin = Financial('1420a551-b76c-4ef1-902d-49226777e0ec',create_time)
    fin.express_resolve(name)
    #exec('print 1+3+4')


    # eval:计算字符串中的表达式
    # exec:执行字符串中的语句
    # execfile:用来执行一个文件
