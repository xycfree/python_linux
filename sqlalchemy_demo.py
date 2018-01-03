#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-27 22:28:27
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import MySQLdb
from sqlalchemy import create_engine,Table,MetaData,Column,Integer,String,tuple_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

db_info = {
    'host' : "127.0.0.1",
    'port' : 3306,
    'user' : 'root',
    'passwd' : 'root',
    'db' : 'aops',
    'charset' : 'utf8'
    }

DB_URI = 'mysql://root:root@127.0.0.1/aops'

# try:
#     con = MySQLdb.connect(db_info['host'],db_info['user'],db_info['passwd'],db_info['db'])
#     cur = con.cursor()
#     cur.execute('SELECT VERSION()')
#     print cur.fetchone()
# except Exception, e:
#     raise e
eng = create_engine(DB_URI)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=eng))

Base = declarative_base()


def init_db():
    # 在这里导入所有的可能与定义模型有关的模块，这样他们才会合适地
    # 在 metadata 中注册。否则，您将不得不在第一次执行 init_db() 时
    # 先导入他们。
    Base.metadata.create_all(bind=eng)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)



if __name__ == '__main__':

    # init_db()
    u = Users('admin12','admin12@163.com')
    # db_session.add(u)
    # db_session.commit()
