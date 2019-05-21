# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:46:07 2019

@author: Sammu
"""

import numpy as np
x=np.random.randint(5,16,40)
#dict1={}
#list1=[]
#count=0
#for i in x:
#    if i not in list1:
#        dict1[i]=1
#        
#    else:
#        count=count+1
#        dict1[i]=count
#print(dict1) 
from collections import Counter
my_counter=Counter(x)
print(my_counter.most_common()[0][0]) 
#z=max(my_counter.values())
#for values,keys in my_counter.item(): 
#    if values==z:
#        print(keys)
        
    
      
        