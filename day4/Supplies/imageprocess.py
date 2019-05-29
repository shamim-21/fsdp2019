# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:59:58 2019

@author: Sammu
"""

from PIL import Image
img=Image.open("sample1.jpg").convert('LA')
img.save("shamim1.png")
img.show()
img_rotate=img.rotate(90)
img.save("shamim2.png")
img_rotate.show()
#crop_im = img.crop(size = (160, 204))
#crop_im.show()
width, height = img_rotate.size
hw = width/2
hh = height/2

img_rot = img_rotate.crop((hw-80,hh-102,hw+80,hh+102))
img_rot.show()
img_rot.thumbnail((75,75))
img_rot.save("shamim3.png")
img_rot.show()
