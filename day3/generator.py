# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:19:10 2019

@author: Sammu
"""
list1=[]
number=input("enter no").split(",")
for i in number:
    list1.append(i)
print("list = ",list1)
tuple1=tuple(number)
print("tuple= ",tuple1)