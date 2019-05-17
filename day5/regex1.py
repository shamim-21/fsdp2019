# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:15:38 2019

@author: Sammu

? = 0 or 1 occurance
* = 0 or more occurance
+ = 1 or more occurance
"""

import re
number=input("enter number =")
result=re.match(r'^[+-]?\d*\.\d+$',number)
if result:
    print(True)
else:
    print(False)
    
"""3.3.3.3
222.333
+-2.33
-.56
+23.
+555.336"""
