# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:51:26 2019

@author: Sammu
"""
with open("new.txt","r")as fp:
    with open("shamim.txt","w") as sb:
        for value in fp:
            sb.write(value)
            
    



