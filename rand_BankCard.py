#!/usr/bin/env python
#coding:utf-8
__author__ = 'xycfree'
import os
import random
'''
    随机生成银行卡号
    卡号长度16位，卡bin,6位 地区 2位，自定义7位 校验位 1位
    622618 02 1688888 8
    前15或18位反转，然后下标偶数位/奇数位*2，如大于等于10，则减9，所有数字相加，取模10，余为0,则返，否则10-余
'''
CARD_BIN = '622618'
AREA = '02'
verify = ''

#生成自定义7位数，不足前补0
def ran_card():
    #c = random.randint(0,9999999)
    ca ='{:0>7}'.format(random.randint(0,9999999))
    #print ca
    return ca

def counts(card):
    #卡号转换为列表形式并倒序排列
    li = list(card)
    li.reverse()
    #偶数下标位*2
    even_num=[ int(x)*2 for i,x in enumerate(li) if not i%2]
    #奇数下标位
    odd_num = [int(x) for i,x in enumerate(li) if i%2]
    num =even_num + odd_num
    sum = 0
    for i in num:
        if i >=10:
            #sum =sum+ int(str(i)[0]) + int(str(i)[1])
            sum += (i - 9)
        else:
            sum += i

    if sum % 10 ==0:
        sum = 0
    else:
        sum = 10 - sum % 10

    return str(sum)

if __name__ == '__main__':
    if os.path.exists('bankcard.dat'):
        os.remove('bankcard.dat')
    f = open('bankcard.dat','w')
    print "开始生成..."
    for i in range(50000):
        c = ran_card()
        card = CARD_BIN + AREA + c
        #print 'card = %s' %card
        bankcard =card + counts(card)
        #print bankcard
        f.write(bankcard+','+'\n')
    f.close()
    print '生成结束!!'
