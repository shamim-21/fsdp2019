# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:53:35 2019

@author: Sammu
"""

import pandas as pd
import numpy as np

df = pd.read_csv("breast_cancer.csv") 
df.isnull().any(axis=0)
df.info()
list1 = df['G'].value_counts()
df['G'] = df['G'].fillna(1.0)

features = df.iloc[:,1:-1].values
labels = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
features_train , features_test , labels_train , labels_test = train_test_split (features , labels , test_size=0.2 , random_state = 0)

from sklearn.svm import SVC
classifier = SVC(kernel='rbf', random_state =0)
classifier.fit(features_train , labels_train)

pred = classifier.predict(features_test)

x=[6,2,5,3,2,7,9,2,4]
x = np.array(x)
x = x.reshape(1 ,-1)
print(classifier.predict(x))


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test , pred)
Score = classifier.score(features_test , labels_test)

classifier = SVC(kernel='poly', random_state =0)
classifier.fit(features_train , labels_train)

pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test , pred)
Score = classifier.score(features_test , labels_test)
