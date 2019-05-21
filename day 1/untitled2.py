# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:22:33 2019

@author: Sammu
"""
i=0
while i<101:
    if i%5==0:
        print("fizz")
    elif i%3==0:
        print("buzz")
    elif i%15==0:
        print("fizz buzz")
    else:
        print(i)
    i=i+1   