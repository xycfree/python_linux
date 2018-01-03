#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/4/11 17:02
# @Descript: 

import autopy
import time

autopy.mouse.move(312, 280)
time.sleep(5)
autopy.mouse.smooth_move(350, 350)