# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:47:18 2019

@author: Sammu
"""

str1=input("enter days")
y=str1.split(",")
new_list=[]
abc=("mon","tues","wed","thurs","fri","sat","sun")
if abc not in y:
    new_list.append(abc)
    print(new_list)

