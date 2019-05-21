# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:26:16 2019

@author: Sammu
"""
import numpy as np
list2=[]
number=input("enter no")
y=number.split(" ")

list2=[int(i) for i in y]
x=np.array(list2)


x=x.reshape(3,3)
print(x)

