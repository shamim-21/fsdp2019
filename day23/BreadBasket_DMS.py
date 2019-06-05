# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:01:10 2019

@author: Sammu
"""

import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("BreadBasket_DMS.csv")
df['Item']= df['Item'].replace("NONE",np.nan)
df = df.dropna(axis = 0)
series = df["Item"].value_counts()
explode = (0.15,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

plt.pie(series.values[0:15], explode = explode, labels=series.index[0:15])
plt.axis('equal') 
plt.show()

#transactions = []
transactions = list(df.groupby(['Transaction'])['Item'].apply(lambda x: list(set(x))))

#for i in range(0,20507):
#    transactions.append([str(df.values[i,j]) for j in range(-2 , -1)])

rules = apriori(transactions, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

results = list(rules)

for item in results:

    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    print("Support: " + str(item[1]))


    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
