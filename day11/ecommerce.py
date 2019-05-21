# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:03:08 2019

@author: Sammu
"""
import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
plt.hist(incomes,bins=50)
x=np.mean(incomes)
y=np.median(incomes)
print("mean=",x)
print("median=",y)
incomes=np.append(incomes,1000000000)
plt.hist(incomes,bins=50)
z=np.mean(incomes)
w=np.median(incomes)
print("mean=",z)
print("median=",w)