#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author: xycfree 
# @Date: 2018-06-19 11:50:52 
# @Descipts: 工厂模式

class Factory:

    def create_fruit(self, fruit):
        if fruit == 'apple':
            return Apple()
        elif fruit == 'banana':
            return Banana()

class Fruit:
    def __str__(self):
        return 'fruit'

class Apple(Fruit):
    def __str__(self):
        return 'apple'


class Banana(Fruit):
    def __str__(self):
        return 'banana'

if __name__ == '__main__':

    factory = Factory()
    print(factory.create_fruit('apple'))
    print(factory.create_fruit('banana'))
