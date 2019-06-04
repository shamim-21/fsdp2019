# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:37:27 2019

@author: Sammu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("monster_com-job_sample.csv")
df1 = df.iloc[:,[-6, -5]]

import re
def func(val1, val2)  :
    val1 = df1['organization']
    val2 = df1['location']
   result=re.search(r'^\D,\D+$',val1)
   if result in val1:
       val1 = val2
       val2 = val1
return ()       
       

    
df1[[col1,col2]] = df1.apply(lambda x: func(x[col1],x[col2]) )     
