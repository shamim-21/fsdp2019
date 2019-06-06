# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:22:49 2019

@author: Sammu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv") 
series = df['Country'].value_counts()


x = plt.pie(series.values, explode = None, labels=series.index)
plt.axis('equal') 
plt.legend()
plt.show()

series1 = df['Classification'].value_counts()


x = plt.pie(series1.values[0:2], explode = None, labels=series1.index[0:2])
plt.axis('equal') 
plt.legend()
plt.show()

