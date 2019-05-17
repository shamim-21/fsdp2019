# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:59:11 2019

@author: Sammu
"""

#pallindromic integer
list1=('1','35','44','-45','3')
for item in list1:
    if int(item)<0:
        print("false")
        break
for value in item:
    if value == value[::-1]:
        print("true")
        break

all_pos = True
palindrome = False

for item in list1:
    if int(item) < 0:
        all_pos = False

if all_pos:
    for i in list1:
        if i == i[::-1]:
            palindrome = True

if palindrome:
    print(True)
else:
    print(False)

   
        
    