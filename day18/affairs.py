# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:24:38 2019

@author: Sammu
"""

import pandas as pd
import numpy as np

df = pd.read_csv("affairs.csv")
features = df.iloc[:,:-1].values
labels = df.iloc[:,-1].values

ohe_objs= []
from sklearn.preprocessing import OneHotEncoder
oh=OneHotEncoder(categorical_features=[6])
features=oh.fit_transform(features).toarray()
features=features[:,1:]
ohe_objs.append(oh)

oh=OneHotEncoder(categorical_features=[-1])
features=oh.fit_transform(features).toarray()
features=features[:,1:]
ohe_objs.append(oh)


from sklearn.model_selection import train_test_split
features_train , features_test , labels_train , labels_test = train_test_split(features , labels , test_size=0.2 , random_state=0)

#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#features_train = sc.fit_transform(features_train)
#features_test = sc.transform(features_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

Score = classifier.score( features_test,labels_test )

val = np.array([[3,25,3,1,5,16,4,2]])
val = ohe_objs[0].transform(val).toarray()
val = val[:,1:]
val = ohe_objs[1].transform(val).toarray()
val = val[:,1:]
classifier.predict(val)
