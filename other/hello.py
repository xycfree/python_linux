#!/usr/bin/env python
from __future__ import unicode_literals
# coding:utf-8

print "hello"
li = [0, 1, 2, 3, 4, 7]
phone = ''
for i in (1, 3, 5, 2, 0, 0, 2, 5, 4, 0, 0):
    phone += str(li[i])
print phone

i = 1
while i < 5:
    if i <> 3:
        print i
        i += 1
    else:
        i += 1
        continue

i = 1
for i in range(5):
    print i

for name, age in (("aabbb", 14),):
    print name
    print age
