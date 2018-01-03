#!/usr/bin/env python
# coding:utf-8
# File:excel2mysql

import os, datetime
import MySQLdb
import xlrd
import sys


def excel_to_mysql(files):
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='jfpython', port=3306, charset='utf8')
    cursor = conn.cursor()
    # cursor.execute("SET NAMES utf8")
    # cursor.execute("SET CHARACTER_SET_CLIENT=utf8")
    # cursor.execute("SET CHARACTER_SET_RESULTS=utf8")

    cursor.execute("SElECT * FROM excels")
    # rs = cursor.fetchall()
    now = int(cursor.rowcount)  # 获取数据行数
    print('now = ', now)

    for n in range(now):
        f = cursor.fetchone()  # 每次查询一条
        for a in f:
            print(a)
        print('\n')

    # 打开excel
    wb = xlrd.open_workbook(files)
    # 获取第一个sheet页
    sh = wb.sheet_by_index(0)
    rowContent = []  # 存储数据
    nrows = sh.nrows  # 行
    ncols = sh.ncols  # 列

    for row in range(1, nrows):

        for col in range(ncols):
            rowContent.append(sh.cell(row, col).value)

        val = ''
        for i in rowContent:
            val = val + unicode(str(i)).encode('utf-8') + ','

        rowContent = []

        val = val[:-1]
        # print 'val = :', val
        li = val.split(',')
        # print li[1].decode('utf-8').encode('utf-8')
        tu = tuple(li)
        print('####################')
        for t in tu:
            print(t)
        print('\n')
        stmt = "INSERT INTO excels (userid,name,age,phone,email,company,job,addr) VALUES ( %s,%s, %s,%s, %s,%s, %s,%s)"
        # stmt = "INSERT INTO excels (userid,name,age,phone,email,company,job,addr) VALUES (%s)"
        cursor.execute(stmt, tu)
        conn.commit()
    # conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    files = r'C:\Users\Administrator\Desktop\file_excel.xlsx'
    print(files)
    excel_to_mysql(files)
