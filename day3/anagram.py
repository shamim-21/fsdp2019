# -*- coding: utf-8 -*-
"""
Created on Sun May 26 00:22:42 2019

@author: Sammu
"""

str1=" ".join("saqeeb")
str2=" ".join("beeqsa")
y=str1.split(" ")
z=str2.split(" ")
y.sort()
z.sort()
#str1.sort()
#str2.sort()
#for i in y:
#    if i not in z:
#        print("not anagram")
#    else:
#        print("anagram")
if y==z:
    print("anagram")
else: 
    print("not anagram")





