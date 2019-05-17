# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:55:47 2019

@author: Sammu
"""

#REPLACING OF CHARACTERS
str1=input("Enter String: ")
rep = input("Enter Char to replace: ")
ch = input("Enter Char to replace with: ")
pos = str1.find(rep)
x=str1[pos+1:].replace(rep,ch)
print(str1[:pos+1]+x)