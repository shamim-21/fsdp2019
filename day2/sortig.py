# -*- coding: utf-8 -*-
"""
Created on Sun May 19 13:59:34 2019

@author: Sammu
"""

list1=[]
while True:
    name=input("enter name,age,height=")
    if not name:
        break
    user_name,age,height=name.split(",") 
    list1.append((user_name,int(age),int(height))) 
list1.sort()
print(list1)    
