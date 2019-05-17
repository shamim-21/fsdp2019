# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:34:25 2019

@author: Sammu
"""
import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['007', '008', '009']
#for i in range(len(names)):
#    names[i] = random.choice(code_names)
#print (names)
list1=[random.choice(code_names) for i in range(len(names))]
def xyz(x):
    return random.choice(code_names)

list3=(list(map(lambda x:random.choice(code_names),names)))