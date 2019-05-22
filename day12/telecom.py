# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:06:12 2019

@author: Sammu
"""

import pandas as pd
df=pd.read_csv("Telecom_churn.csv")
df['churn'][(df['international plan']=='yes')& (df['voice mail plan' ]=='yes')].value_counts()




