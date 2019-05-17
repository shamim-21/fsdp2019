# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:23:44 2019

@author: Sammu
"""
import csv    
dict1={}
with open("passwd", "r") as file1:
   file2=csv.reader(file1,delimiter=":")
   for row in file2:
       dict1[row[0]]=row[2]

        