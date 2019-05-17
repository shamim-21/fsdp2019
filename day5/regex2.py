# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:04:20 2019

@author: Sammu
"""
import re
list=[]
while True:
    
    email=input("enter email")
    if not email:
        break
    result=re.match(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+.[a-zA-Z]{2,4}$',email)
    
    if result:
        list.append(email)
    else: 
        print("invalid email")
    
    
    
   