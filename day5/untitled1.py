# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:09:10 2019

@author: Sammu
"""

import re
list1 = []
with open("simpsons_phone_book.txt","r") as file:
    for i in file: 
        val = re.search(r'^J.*Neu', i)
        if val:
            list1.append(i.strip())
print(list1)
        