# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:05:25 2019

@author: Sammu
"""

import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Market_Basket_Optimisation.csv", header = None)
#transactions = []

#list1 = list(df.apply(lambda x: list(set(x))))

#for i in range(0, 7501):
#    transactions.append([str(df.values[i,j]) for j in range(0, 20)])
#    
    
trans = df.applymap(lambda x:[x] if pd.notnull(x) else []).sum(1).tolist()

rules = apriori(trans, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

results = list(rules)

for item in results:

    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    print("Support: " + str(item[1]))


    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    
