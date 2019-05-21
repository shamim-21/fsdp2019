# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:35:17 2019

@author: Sammu
"""

#reverse function


str1=input("Enter a text ")
temp=""
i=-1
while i>=(-len(str1)):
    temp=temp+str1[i]
    i=i-1
print(temp)
