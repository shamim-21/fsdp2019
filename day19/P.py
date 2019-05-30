# -*- coding: utf-8 -*-
"""
Created on Thu May 30 18:26:15 2019

@author: Sammu
"""

import pandas as pd
import numpy as np

df = pd.read_csv("PastHires.csv")

features = df.iloc[:,:-1].values
labels = df.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
le1 = LabelEncoder()
features[:,1] = le1.fit_transform(features[:,1])

le2 = LabelEncoder()
features[:,3] = le2.fit_transform(features[:,3])

le3 = LabelEncoder()
features[:,4] = le3.fit_transform(features[:,4])

le4 = LabelEncoder()
features[:,5] = le4.fit_transform(features[:,5])

features = features.astype(int)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20, random_state=0)

from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred)) 

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred))  
