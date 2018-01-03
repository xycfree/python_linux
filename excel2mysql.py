#!/usr/bin/env python
#coding:utf-8
#File:excel2mysql
import os,datetime
import MySQLdb
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def excel_to_mysql(files):
    
    wb = xlrd.open_workbook(files)
    sh = wb.sheet_by_index(0)
    dfun = []
    nrows = sh.nrows
    ncols = sh.ncols
    fo = []
    sql_tab  = 'id int(6) auto_increment primary key, '
    fo.append(sh.row_values(0))
    print "���ݱ�ͷ��",fo
    for i in range(1,nrows):
        dfun.append(sh.row_values(i))
    print "��������:",dfun

    conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='jfpython',port=3306,charset='utf8')
    cursor = conn.cursor()
    for i in range(ncols):
        sql_tab = sql_tab + fo[0][i] + ' varchar(255) ,'

    sql_tab = sql_tab[:-1]
    cursor.execute("create table excels (" + sql_tab +");")
    val = ''
    for i in range(0,ncols):
        val = val + '%s,'
    print dfun
    cursor.executemany("insert into excels values(" + val[:-1] + ");",dfun)
    conn.commit()
    cursor.close()
if __name__ == '__main__':
    files = r'C:\Users\Administrator\Desktop\file_excel.xlsx'
    print files
    excel_to_mysql(files)