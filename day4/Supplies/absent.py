# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:00:31 2019

@author: Sammu"""

with open("absent.txt","w")as file:
    i=0
    while (i<25):
        item=input(">")
        if not item:
            break
        file.write(item+"\n")
        i=i+1
with open("absent.txt","r")as fp:
    print(fp.read())
        

    
    
    
    
    
    