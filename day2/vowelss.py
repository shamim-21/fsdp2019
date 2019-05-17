# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:19:56 2019

@author: Sammu
"""

#vowels finder
list1=['alabama','california','oklahoma','florida']


new_list = []




for state in list1:
    str1 = ""
    for item in state:
        if item not in "aeiou":
            str1 = str1 + item
    new_list.append(str1)
    print (str1)
