# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:28:31 2019

@author: Sammu
"""
filename = input("Enter a filename: ")
print(open(filename).readlines()[-1])

 