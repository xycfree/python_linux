#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/2/17 11:39
# @Descript: 装饰器,atm系统，存款，取款，转账

class AtmDecorate(object):
    def __init__(self):
        pass

    def user(self, user, passwd):
        pass

    @user
    def deposit(self, money):
        pass

    @user
    def withdraw(self, money):
        pass

    @user
    def transfer(self, bank_name, to_user, to_account, money):
        pass

    @user
    def query(self):
        pass
