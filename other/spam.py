#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-14 11:09:34
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

#字符倒序输出
def str_print(s):
    str1 = s[::-1]
    for i in str1:
        print i

s =raw_input('please input string:')
if len(s) !=0:
    str_print(s)
else:
    print 'error'

a = 'abcde12345'
for i in a[::-1]:
    print i


#拉丁猪游戏
def str_aeiou(s):
    str1 = s
    if str1[0] not in 'aeiou':
        str1 = s[1:] +'-'+ s[0] +'ay'
    else:
        return '首字母不是辅音字符'
    return str1

s = raw_input('please input string:')
if len(s) !=0:
    print str_aeiou(s)
else:
    print 'error'

#统计字符串中元音字符个数
def str_aeiou(str1):
    s ='aeiou'
    count = 0;a=0;e=0;i=0;o=0;u=0

    for j in str1:
        if j in s:
            count +=1
            if j == 'a': 
                a += 1
            elif j == 'e': 
                e += 1
            elif j == 'i':
                i += 1
            elif j =='o':
                o += 1
            else:
                u += 1

    return (count,a,e,i,o,u)


s = raw_input('please input string:')
if len(s) !=0:
    print str_aeiou(s)
else:
    print 'error'


#判断是否为回文
def str_go(strs):
    lens = len(strs)/2

    if len(strs) % 2 ==0:
        str1 = strs[0:lens]
        str2 = strs[-1:lens-1:-1]
        print str1,str2
        if str1 == str2:
            return True
        else:
            return False
    else:
        str1 = strs[0:lens]
        str2 = strs[-1:lens:-1]
        print str1,str2
        if str1 == str2:
            return True
        else:
            return False


s = raw_input('please input string:')
if len(s) >=2 :
    print str_go(s)
else:
    print 'error'


a = 'false true hello world    a is two de '
li = a.split()
print len(li)

b ='false.true,hello;world?a two'
li = b.split(' ')
print len(li)



