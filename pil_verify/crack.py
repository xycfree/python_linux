#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/12 14:27
import hashlib
import time
import os
import math
from PIL import Image

class VectorCompare:
    def magnitude(self,concordance):
        total = 0
        for word, count in concordance.iteritems():
            total += count ** 2
        return math.sqrt(total)

    def relation(self, concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.iteritems():
            if concordance2.has_key(word):
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))

def build_vector(im):
    d1 = {}
    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1

v = VectorCompare()
iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
image_set = []
for letter in iconset:
    for img in os.listdir('./python_captcha/python_captcha/iconset/%s/' % (letter)):
        temp = []
        if img != 'Thumbs.db' and img != '.DS_Store':
            temp.append(build_vector(Image.open('./python_captcha/python_captcha/iconset/%s/%s' %(letter,img))))
        image_set.append({letter:temp})


im = Image.open('verify1.jpg')
im.convert('P')  # 将图片转换为8位像素模式
print(im.histogram())  # 打印颜色直方图
temp = {}
his = im.histogram()  # 颜色直方图
values = {}

for i in range(256):
    values[i] = his[i]

for j,k in sorted(values.items(),key=lambda x:x[1], reverse=True)[:10]:
    print('{0},{1}'.format(j, k))

im2 = Image.new('P', im.size, 255)
for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        if pix == 220 or pix == 227:  # 得到数字
            im2.putpixel((y, x), 0)
im2.show()  # 显示黑白二值图片

inletter = False
found_letter = False
start = 0
end = 0
letters = []

for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y,x))
        if pix != 255:
            inletter = True
    if found_letter == False and inletter == True:
        found_letter = True
        start = y

    if found_letter == True and inletter == False:
        found_letter = False
        end = y
        letters.append((start, end))
    inletter = False
print(letters)

count = 0
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
    # m.update('%s%s' % (time.time(), count))
    # im3.save('./%s.gif' % (m.hexdigest()))
    # count += 1

    guess = []
    for image in image_set:
        for x, y in image.iteritems():
            if len(y) != 0:
                guess.append((v.relation(y[0],build_vector(im3)),x))

    guess.sort(reverse=True)
    print('guess is:{}'.format(guess[0]))

    count += 1








