# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:39:01 2019

@author: Sammu
"""

import numpy as np
import pandas as pd

df = pd.read_csv("iq_size.csv")
features = df.iloc[:,1:].values
labels = df.iloc[:,0].values

import statsmodels.api as sm
features = sm.add_constant(features)
features_opt = features[:, [0,1,2,3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [0,1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
regressor_OLS.params
regressor_OLS.predict(90)





