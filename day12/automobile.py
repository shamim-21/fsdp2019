# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:48:49 2019

@author: Sammu
"""

import pandas as pd
import numpy as np
df=pd.read_csv("Automobile.csv")
df['price']=df['price'].fillna(df['price'].mean())
x=np.array(df['price'])
np.min(x)
np.max(x)
np.std(x)
np.mean(x)
