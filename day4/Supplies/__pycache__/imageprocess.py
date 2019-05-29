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
#img.save("shamim2.png")
img_rotate.show()