# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:02:43 2019

@author: Sammu
"""

#translate function
str1="AEIthis is fun"
i=0
temp=""
while i<11:
    if str1[i] not in " AEIOU aeiou":
        temp=temp +str1[i]+"o"+str1[i]
        
    else:
        temp=temp+str1[i]
        
        
        
    i=i+1
print(temp)
        
        
        