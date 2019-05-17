# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:56:22 2019

@author: Sammu
"""

names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print (names)
list1=[hash(names[i]) for i in range(len(names))]
def fun(x):
    return hash(x)
list2=(list(map(lambda x:hash(x),names)))
list3=list(map(fun,names))