# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:06:12 2019

@author: Sammu
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Telecom_churn.csv")
df['churn'][(df['international plan']=='yes')& (df['voice mail plan' ]=='yes')].value_counts()
df['total intl charge'][(df['churn']==True)].sum()
df['total intl charge'][(df['churn']==False)].sum()
df1=df[df['churn']==True]
max1=df1['total night minutes'].max()
df['state'][(df['total night minutes']==max1)]

