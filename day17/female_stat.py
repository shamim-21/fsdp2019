# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:37:38 2019

@author: Sammu
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("Female_Stats.csv")
features = df.iloc[:,1:].values
labels = df.iloc[:,0].values
#plt.scatter(features[:,1],labels)

import statsmodels.api as sm
features = sm.add_constant(features)
features_opt = features[:, [0,1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
regressor_OLS.params
print("both are significant for  student")


#features_mom=df.iloc[:,1:2].values
#labels_mom=df.iloc[:,0].values
#features_opt = features[:, [0, 1, 2, 3, 4, 5]]
#regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
#regressor_OLS.summary()
#
