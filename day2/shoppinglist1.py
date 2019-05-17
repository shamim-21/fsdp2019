# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:42:23 2019

@author: Sammu
"""

shopping_list=[]
print("enter item")
print("done for stop adding")
while True:
    
    new_list=input("*")
    if new_list=='done'or new_list=='Done'or new_list=='DONE':
        break
    if new_list=="show" or new_list=="Show" or new_list=="SHOW":
        print(shopping_list)
        new_list=""
    elif new_list=="help"or  new_list=="Help" or  new_list=="HELP":
        print("bhai\n list\n dek \nlena\n bad\n mn")
        
    shopping_list.append(new_list)
print("HERE IS YOUR LIST")
i=0
for item in shopping_list:
    i=i+1
    print(str(i)+" "+item)