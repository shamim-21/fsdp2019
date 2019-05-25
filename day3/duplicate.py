# -*- coding: utf-8 -*-
"""
Created on Sun May 26 00:15:27 2019

@author: Sammu
"""

list1=[12,24,35,24,88,120,155,88,120,155]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        list2.remove(i)