# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:16:55 2019

@author: Sammu
"""




from collections import OrderedDict

dict1 = OrderedDict()
dict2={}
while True:
    item=input(">")
    if not item:
        break
    list1=item.split(" ")
    keys=list1[0:-1]
    keys=" ".join(keys)
    values=int(list1[-1])
    
   
    if keys in dict2:
        values=values+dict2.get(keys)
    dict2[keys]=values
for k in dict2:
    print(k,dict2[k])
#dict1[keys] = values
#if keys not in list1:
#    list1.update()
    
"""dict1[keys] = dict1.get(keys,0) + values
print(dict1[keys])"""

