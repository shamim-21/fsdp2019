# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:38:00 2019

@author: Sammu
"""

#leap year
year = int(input("enter year"))
def calculater(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print("leap year")
    else:
        print("not a leap year")    
calculater(year)    