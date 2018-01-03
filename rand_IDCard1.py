#!/usr/bin/env python
#coding:utf-8
__author__ = 'xycfree'
import os
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import random

'''身份证号码生成脚本
   根据省份，市，县编号，生日，顺序，校验码生成；
'''
#省份 代码
'''
province = {'北京':'11','天津':'12','河北':'13','山西':'14','内蒙':'15',
          '辽宁':'21','吉林':'22','黑龙':'23',
          '上海':'31','江苏':'32','浙江':'33','安徽':'34','福建':'35','江西':'36','山东':'37',
          '河南':'41','湖北':'42','湖南':'43','广东':'44','广西':'45','海南':'46',
          '重庆':'50','四川':'51','贵州':'52','云南':'53','西藏':'54',
          '陕西':'61','甘肃':'62','青海':'63','宁夏':'64','新疆':'65'}
          #香港 81  台湾 71 澳门 82 国外 91
'''

province = {'北京':'11','天津':'12','河北':'13'}
#市 代码
#city = ['01','02','03','04','05','06','07','08','09','10']
city = ['01','02']
#县 代码
county = ['01','02','03','04','05','06','07']
#系数 校验位计算系数coefficient
coeff = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
#号码通过系数相乘求和与11取余得出校验码
mod_coeff = [1,0,'X',9,8,7,6,5,4,3,2]
'''
def gen_str():
    no_1 = str(random.choice(province.values())) #省
    no_2 = str(random.choice(city)) #市
    no_3 = str(random.choice(county)) #县/区

    no_4 = str(random.randrange(1949,2011)) #出生年
    no_5 = '{:0>2}'.format(str(random.randrange(01,13))) #出生月 小于10要补0
    #no_6 = '{:0>2}'.format(str(random.randrange(01,32))) #出生日 小于10补0，判断单月，双月，闰月
    no_6 = generate_day(no_4,no_5)
    no_7 = '{:0>3}'.format(str(random.randrange(001,999))) #'{:0>3}'.format('111')
    no_8 = no_1 + no_2 + no_3 + no_4 + no_5 + no_6 + no_7
    return no_8
'''
#根据前17位数字算出第18位校验位
def verify_code(no_8):
    num = 0
    for i in range(len(no_8)):
        num += int(no_8[i]) * coeff[i]
    m = num % 11 #求余
    for i in range(11):
        if i != m:
            continue
        verify = mod_coeff[i]
    return str(verify)

#闰年
def generate_day(no_4,no_5):

    if isleap_year(no_4):
        global day
        if no_5 == '02':
            day = '{:0>2}'.format(str(random.randrange(01,30)))
        else:
            day = days(no_5)
    else:
        day = days(no_5)
    return day

#平年
def days(no_5):
    if no_5 =='02':
        day = '{:0>2}'.format(str(random.randrange(01,29)))
    elif no_5 in ['01','03','05','07','08','10','12']:
        day = '{:0>2}'.format(str(random.randrange(01,32)))
    else:
        day = '{:0>2}'.format(str(random.randrange(01,31)))
    return day



#判断是否为润年
def isleap_year(no_4):
    if (int(no_4) % 4 ==0 and int(no_4) % 100 !=0) or int(no_4) % 400 ==0:
        return True
    else:
        return False

if __name__ == '__main__':
    if os.path.exists('idcard.dat'):
        #f = open('idcard.txt','a')
        os.remove('idcard.dat')
    f = open('idcard.txt','w')
    print "开始生成..."#.decode('utf-8')
    for i in range(50000):
        #print "开始执行第%d次..." %i
        no_1 = str(random.choice(province.values())) #省
        no_2 = str(random.choice(city)) #市
        no_3 = str(random.choice(county)) #县/区
        no_4 = str(random.randrange(1950,2011)) #出生年
        no_5 = '{:0>2}'.format(str(random.randrange(01,13))) #出生月 小于10要补0
        #no_6 = '{:0>2}'.format(str(random.randrange(01,32))) #出生日 小于10补0，判断单月，双月，闰月
        no_6 = generate_day(no_4,no_5)
        no_7 = '{:0>3}'.format(str(random.randrange(001,999))) #'{:0>3}'.format('111')
        no_8 = no_1 + no_2 + no_3 + no_4 + no_5 + no_6 + no_7

        v = verify_code(no_8)
        id = no_8 + v
        f.write(id)
        f.write(',')
        f.write('\n')
        #print "id = ",id
    f.close()
    print "生成结束..."#.decode('utf-8')
