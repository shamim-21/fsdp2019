# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:34:39 2019

@author: Sammu
"""

import pandas as pd
df = pd.read_csv("training_titanic.csv")
#df['Survived'].value_counts()
#surv = df[(df['Survived']==1)]
#
#survive=surv['Survived'].value_counts().tolist()
#died1=df[(df['Survived']==0)]
#died=died1['Survived'].value_counts().tolist()
#surv['Survived'].value_counts(normalize=True)
print("no of survived people",df['Survived'].value_counts()[1])
print("no of dead people",df['Survived'].value_counts()[0])
print("survival rate=",df['Survived'].value_counts(normalize = True)[1])
df['Survived'][df['Sex']=='male'].value_counts(normalize=True)
df['Survived'][df['Sex']=='female'].value_counts(normalize=True)
print(df['Age'])
df['Age'] = df['Age'].fillna(df['Age'].mean())

df["children"] = df["Age"].map(lambda x: 0 if x >18 else 1 )
df['children'].value_counts()[1]




