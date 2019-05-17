# -*- coding: utf-8 -*-
"""
Created on Fri May 10 23:06:26 2019

@author: Sammu
"""
dict1={}
with open("romeo.txt","r") as file:
    list1=file.readlines()
    sha=[]
    for item in list1:
        file.seek(0,0)
       
        word=item.split(" ")
        for value in word:
            sha.append(value)
            new_list=[]
      
            for key in word:
                if key not in new_list:
                    dict1[key]=1
                else:
                    x=dict1.get(key)
                    dict1[key]=x+1
    print(dict1)                
                
        
    
        