# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:22:47 2019

@author: Sammu
"""

list1=[]
i=0
while i<5:
    number=int(input("enter no="))
    list1.append(number)
    i=i+1
def add(list1):
    total=0
    for x in list1:
        total=total+x
    return(total)
def multiply(list1): 
    product=1
    for z in list1:
        product=product*z
    return (product)
def largest(list1):
    x=list1[0]
    for i in list1:
        if x<i:
            x=i
    return x
def smallest(list1): 
    x=list1[0]
    for i in list1:
        if x>i:
            x=i
    return x 
def sorting(list1): 
    list1.sort()
    return list1
def remove_dup(list1):
    list2=[]
    for x in list1:
        if x not in list2:
            list2.append(x)
    return list2   
print(add(list1))
print(multiply(list1))
print(largest(list1))
print(smallest(list1))
print(sorting(list1))
print(remove_dup(list1))     
        
    
    
    