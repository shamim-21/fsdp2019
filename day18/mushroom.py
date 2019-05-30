# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:47:29 2019

@author: Sammu
"""

import pandas as pd
import numpy as np

df = pd.read_csv("mushrooms.csv")
features = df.iloc[:,[5,21,22]].values
labels = df.iloc[:,0].values

from sklearn.preprocessing import LabelEncoder
le1 = LabelEncoder()
features[:,0] = le1.fit_transform(features[:,0])

le2 = LabelEncoder()
features[:,1] = le2.fit_transform(features[:,1])

le3 = LabelEncoder()
features[:,2] = le3.fit_transform(features[:,2])

le4 = LabelEncoder()
labels = le4.fit_transform(labels)


from sklearn.preprocessing import OneHotEncoder
ohe1 = OneHotEncoder(categorical_features=[0])
features = ohe1.fit_transform(features).toarray()
features=features[:,1:]

ohe2 = OneHotEncoder(categorical_features=[-2])
features = ohe2.fit_transform(features).toarray()
features=features[:,1:]

ohe3 = OneHotEncoder(categorical_features=[-1])
features = ohe3.fit_transform(features).toarray()
features=features[:,1:]

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

#odor=a,population=s,habitat=g


val = np.array(['a','s','g']).reshape(1,-1)
val[:,0] = le1.transform(val[:,0])

val[:,1] = le2.transform(val[:,1])
val[:,2] = le3.transform(val[:,2])
val = ohe1.transform(val).toarray()
val = val[:,1:]
val = ohe2.transform(val).toarray()
val = val[:,1:]
val = ohe3.transform(val).toarray()
val = val[:,1:]
classifier.predict(val)

