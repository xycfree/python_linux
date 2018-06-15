#!/usr/bin/env python
#coding:utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import json
#全局变量
URL = 'http://api.map.baidu.com/location/ip'
AK = 'bSierdSvB9ym9AuTaolpObgDlBLc7avX'

def get_addr(ip):
    '''
    百度IP定位API接口，通过requests请求
    '''
    #接口参数
    payload = {
        'ip':ip,
        'ak':AK,
        
    } 
    try:
        r = requests.get(URL,params=payload)
    except Exception,e:
        #print e
        #raise e
        return e
    
    return r.json()
    
result = get_addr(ip='119.57.156.2')
#print result.items()
#
#for (k, v) in dict.items():
#    print "dict[%s] =" % k, v
#调用iteritems()实现字典的遍历
# dict = {"a" : "apple", "b" : "banana", "c" : "grape", "d" : "orange"}
# print dict.iteritems()
# for k, v in dict.iteritems():
#     print "dict[%s] =" % k, v
# for (k, v) in zip(dict.iterkeys(), dict.itervalues()):
#     print "dict[%s] =" % k, v

#遍历嵌套字典并打印
def isdict(di):
    if isinstance(di, dict):
        print '嵌套key: ',di.keys()[0]
        for (k,v) in di.items():
            print k,v
            isdict(v)




print len(result)

if result['status']:
    print '请求失败！！'
    for k in result.keys():
        print k,result[k]
else:
    print '请求成功！！'
    for k,v in result.items():
        if isinstance(v,dict):
            print 'key: ',k
            isdict(v)
        else:
            print k,v

        #print k,result[k]
    #print json.dumps(result)


print get_addr.__doc__
