# -*- coding: utf-8 -*-
"""
Created on Sat May 25 23:34:45 2019

@author: Sammu
"""
dict1={}
str1="python 3.2"
dict1["digits"]=0
dict1["letters"]=0
for item in str1:
    if item.isalpha():
        dict1["letters"]=dict1["letters"]+1
    elif item.isdigit():
        dict1["digits"]=dict1["digits"]+1
for keys,values in dict1.items():
    print(keys,values)
       
    
    
    