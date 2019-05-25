# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:46:03 2019

@author: Sammu
"""
"""from colletions import orderedDict"""
str1="www.goo gle.com"
"""new_list = orderedDict()"""
dict1={}
y=" ".join(str1)
list1=y.split()

for item in list1:
    if item not in dict1:
        dict1[item]=1      
    else:
        x=dict1.get(item) 
        dict1[item]=x+1 
print(dict1)

#for i in list1:
#    if i in new_list:
#        new_list[i]+=1
#    else:
#        new_list[i]=1

