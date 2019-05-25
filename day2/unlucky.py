# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

str1="13,1,2,13,2,1,13"
y=str1.split(",")
total=0

i=0
while i < len(y):
    print(i)
    if int(y[i])==13:
        i=i+2
        
    else:
        total=total+int(y[i])
        i=i+1
     
    
    