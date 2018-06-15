#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/9 19:07

from pil_verify import Image, ImageFilter
kitten = Image.open("kitten.jpg")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("kitten_blurred.jpg")
blurryKitten.show()