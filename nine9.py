#!/usr/bin/env python
#coding:utf-8

for i in range(1,10):
    for j in range(1,i+1):
        print str(j) + ' * ' + str(i) + ' = '+ str(i*j) +' ',
    print '\n' 

for i in range(1,10):
    for j in range(1,i+1):
        c = i * j
        print '{i} * {j} = {c}  '.format(i=i,j=j,c=c) +' ',
    print '\n' 

    
