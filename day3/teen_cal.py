# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:26:51 2019

@author: Sammu
"""
list1=[13,14,17,18,19]
dict1={"a":2,"b":15,"c":13}
"""dict1[keys]=values"""
sum=0
for values in dict1.values():
    if values in list1:
        values=0
#        y=sum(dict1.values())
#        print(y)
    else:
        sum=sum+values
print(sum)
