# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:06:11 2019

@author: Shamim
"""
list1=input("enter nos")
list2=list1.split(" ")
print(all([int(i)>0 for i in list2])and any([i==i[::-1] for i in list2]))
        
    
    
    
    


    
    
    
    
    
    

