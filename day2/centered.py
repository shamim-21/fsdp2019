# -*- coding: utf-8 -*-
"""
Created on Sun May 19 14:26:41 2019

@author: Sammu
"""

number=input("enter number")
x=number.split(",")
list1=[]
list1=[int(i) for i in x]
list1.sort()
avg=sum(list1[1:len(list1)-1])/(len(list1)-2)
