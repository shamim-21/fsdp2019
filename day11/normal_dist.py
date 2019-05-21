# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:44:36 2019

@author: Sammu
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(150.0, 20.0, 1000)
plt.hist(incomes,bins=100)
x=np.std(incomes)
y=np.var(incomes)
print("standard deviation=",x)
print("variance=",y)

