#!/usr/bin/env python
#coding:utf-8
#python在windows锁屏的代码

import os 
from ctypes import *
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

user32 = windll.LoadLibrary('user32.dll')
user32.LockWorkStation()
