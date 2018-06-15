#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/4/12 20:16
# @Descript: 

import qrcode

qrcode.generate('Hello world!')

qrcode.generate('Python QR code!', width=420, filename='kitten.jpg')

qrcode.scan('kitten.jpg')

qrcode.scan('kitten.jpg')

# Exception raised here, as version 1 QR code cannot encode
# more than 17 characters in byte mode.
qrcode.generate('012345678901234567')