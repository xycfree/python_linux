#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-06 21:53:49
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import MySQLdb
import time

def db_object():
    db_info={
        'host':'101.200.203.42',
        'port':3306,
        'user':'pcode',
        'passwd':'0+1+3=4',
        'db':'finance_analyse',
        'charset':'utf8'} #定义数据库连接信息

    db_info1 = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': 'root',
            'db': 'finance_analyse',
            'charset': 'utf8'}  # 定义数据库连接信息

    try:
        conn = MySQLdb.connect(**db_info)
        cur = conn.cursor()
        return conn,cur
    except  MySQLdb.Error,e:
        print "Mysql Error {arg0}:{arg1}".format(arg0=e.args[0],arg1=e.args[1])
    '''
    finally:
        cur.close()
        conn.close()
    '''
#条件查询
def db_select_on(query):
    cur = db_object()[1]
    cur.execute(query)
    row = cur.fetchone()
    return row

#模糊全部
def db_select_all(query):
    cur = db_object()[1]
    cur.execute(query)
    row = cur.fetchall()
    return row

# 单条插入，成功返回1，失败返回None
def db_insert_on(query,*args):
    try:
        conn,cur = db_object()
        result = cur.execute(query,*args)
        conn.commit()
        return result
    except MySQLdb.Error,e:
        print "Mysql Error {arg0}:{arg1}".format(arg0=e.args[0],arg1=e.args[1])


