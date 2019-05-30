# -*- coding: utf-8 -*-
"""
Created on Thu May 30 07:48:17 2019

@author: Sammu
"""



import numpy as np
import pandas as pd
 
df= pd.read_csv("tree_addhealth.csv")
df['age']=df['age'].fillna(df['age'].mean())
df['ESTEEM1']=df['ESTEEM1'].fillna(df['ESTEEM1'].mean())

features=df.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14]].values
labels=df.iloc[:,7].values

from sklearn.model_selection import train_test_split
features_train , features_test , labels_train , labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.fit_transform(features_test)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(features_train , labels_train)

labels_pred = lr.predict(features_test)
 
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test , labels_pred)

Score = lr.score(features_test , labels_test) 

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

labels_pred1 = classifier.predict(features_test)
 
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test , labels_pred1)

Score = classifier.score(features_test , labels_test) 
