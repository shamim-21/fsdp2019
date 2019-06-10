# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:05:59 2019

@author: Sammu
"""

import pandas as pd

df = pd.read_csv("amazon_cells_labelled.txt" , delimiter="\t" , header = None)
df.columns= ["review","liked"]

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0,1000):
    review = re.sub('[^a-zA-Z]', ' ', df['review'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = df.iloc[:, 1].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

"""Naive Bayes"""
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm_nb = confusion_matrix(labels_test, labels_pred)   

from sklearn.metrics import accuracy_score 
 
Score = accuracy_score(labels_test, labels_pred) 

"""Knn"""
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)

labels_pred_knn = classifier.predict(features_test)

cm_knn = confusion_matrix(labels_test, labels_pred_knn)
Score_knn = accuracy_score(labels_test, labels_pred_knn) 
list1 = []
review = "awesome it was beautiful "
review = re.sub('[^a-zA-Z]', ' ', review)
review = review.lower()
review = review.split()
review = [word for word in review if not word in set(stopwords.words('english'))]
review = [ps.stem(word) for word in review]
review = ' '.join(review)
list1.append(review)

features_pred = cv.transform(list1).toarray()
pred = classifier.predict(features_pred)
