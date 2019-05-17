# -*- coding: utf-8 -*-
"""
Created on Wed May  8 23:55:54 2019

@author: Sammu
"""

#pangram
str1="The quick brown fox jumps over the lazy dog"
str1=str1.lower()
str1=" ".join(str1)
list1=str1.split()
new_list=[]
for letter in list1:
    if letter not in new_list:
       new_list.append(letter) #new_list=new_list+letter
       new_list.sort()
       
        
abc="abcdefghijklmnopqrstuvwxyz"
abc=" ".join(abc)
abc=abc.split()
if  (abc==new_list):
    print("Pangram")
else:
    print("not pangram")