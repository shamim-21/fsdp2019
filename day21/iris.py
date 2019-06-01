# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:55:34 2019

@author: Sammu
"""

from sklearn import datasets

df = datasets.load_iris()
features = df.data
labels = df.target

from sklearn.model_selection import train_test_split
features_train , features_test , labels_train , labels_test = train_test_split (features , labels , test_size=0.2 , random_state = 0)

from sklearn.svm import SVC
classifier = SVC(kernel='poly', random_state =0)
classifier.fit(features_train , labels_train)

pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test , pred)
Score = classifier.score(features_test , labels_test)






