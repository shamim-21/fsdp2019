# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:19:14 2019

@author: Sammu
"""


people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},{'name': 'Mary', 'height': 150},
          {'name': 'Isla', 'height': 20} ,{'name': 'Sam'}
         ]
#
#height_total = 0
#height_count = 0
#for person in people:
#    if 'height' in person:
#        height_total += person['height']
#        height_count += 1
#
#if height_count > 0:
#    average_height = height_total / height_count
#
#    print (average_height)
list3=[]
def func(x):
    if 'height' in x:
        list3.append(x['height'])
list(map(func,people))
def add(x,y):
    return x+y
from functools import reduce
avg=reduce(add,list3)/len(list3)
print(avg)



#list1=list(map([height_total += person['height']  height_count += 1 if 'height' in person for person in people])) 
        
          