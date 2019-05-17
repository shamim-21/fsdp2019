# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:48:53 2019

@author: Sammu
"""
month=input("enter month")
year=int(input("Enter Year"))
list1=('january','march','may','july','august','october','december')
list2=('april','june','september','november')
list3=('february')
def no_month(month,year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print("leap year")
        if month in list3:
            print("29")
    else:
        if month in list1:
            print("31")
        elif month in list2:
            print("30")
        elif month in list3:
            print("28")
no_month(month,year)    
    
    