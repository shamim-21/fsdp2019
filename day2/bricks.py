# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:12:15 2019

@author: Sammu
#bricks
"""
x=int(input("enter no of small bricks"))
y=int(input("enter no of big bricks"))
z=int(input("enter the lenght of target"))
list=[x,y,z]
def brick(list):
    if((list[0]*1)+(list[1]*5)>=list[2]):
        print("True")
    else:
        print("False")
        
brick(list)       
