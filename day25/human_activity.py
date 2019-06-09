# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:39:35 2019

@author: Sammu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

test = pd.read_csv("test.csv")
train = pd.read_csv("train.csv")

features_test = test.iloc[:,:-2].values
labels_test = test.iloc[:,-1].values

features_train = train.iloc[:,:-2].values
labels_train = train.iloc[:,-1].values

""" DECISIONTREECLASSIFIER"""
from sklearn.tree import DecisionTreeClassifier  
classifier_dtc = DecisionTreeClassifier()  
classifier_dtc.fit(features_train, labels_train)

labels_pred_dtc = classifier_dtc.predict(features_test) 

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred_dtc))  

from sklearn.metrics import accuracy_score 
 
Score_dtc = accuracy_score(labels_test, labels_pred_dtc)

"""RANDOMFORESTCLASSIFIER"""
from sklearn.ensemble import RandomForestClassifier

classifier_rfc = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier_rfc.fit(features_train, labels_train)  
labels_pred_rfc = classifier_rfc.predict(features_test)


print(confusion_matrix(labels_test,labels_pred_rfc))  
Score_rfc = accuracy_score(labels_test, labels_pred_rfc)

"""LOGISTICREGRESSION"""
from sklearn.linear_model import LogisticRegression
classifier_lr = LogisticRegression()
classifier_lr.fit(features_train , labels_train)
labels_pred_lr = classifier_lr.predict(features_test)


print(confusion_matrix(labels_test,labels_pred_lr))  
Score_lr = accuracy_score(labels_test, labels_pred_lr)

"""KNN"""
from sklearn.neighbors import KNeighborsClassifier
classifier_knn = KNeighborsClassifier(n_neighbors = 5, p = 2) 
classifier_knn.fit(features_train, labels_train)

probability = classifier_knn.predict_proba(features_test)

labels_pred_knn = classifier_knn.predict(features_test)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels_test, labels_pred_knn))
Score_knn = accuracy_score(labels_test, labels_pred_knn)

"""LABELENCODE"""
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels_train = labelencoder.fit_transform(labels_train)
labels_test = labelencoder.fit_transform(labels_test)

import statsmodels.api as sm
features_train = sm.add_constant(features_train)
column=list(range(features_train.shape[1]))

while True:
    features_opt = features_train[:,column]
    regressor_OLS = sm.OLS(endog = labels_train, exog = features_opt).fit()
    p = regressor_OLS.pvalues
    if p.max() < 0.05:
        break
    else:
        val = list(p).index(p.max())
        column.pop(val)
        print("saqeeb")
features_test = sm.add_constant(features_test)
features_opt_test = features_test[:,column]        

""" DECISIONTREECLASSIFIER"""
classifier_dtc1 = DecisionTreeClassifier()  
classifier_dtc1.fit(features_opt, labels_train)

labels_pred_dtc1 = classifier_dtc1.predict(features_opt_test) 

print(confusion_matrix(labels_test, labels_pred_dtc1))  
Score_dtc1 = accuracy_score(labels_test, labels_pred_dtc1)

"""RANDOMFORESTCLASSIFIER"""

classifier_rfc1 = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier_rfc1.fit(features_opt, labels_train)  
labels_pred_rfc1 = classifier_rfc1.predict(features_opt_test)


print(confusion_matrix(labels_test,labels_pred_rfc1))  
Score_rfc1 = accuracy_score(labels_test, labels_pred_rfc1)

"""LOGISTICREGRESSION"""
classifier_lr1 = LogisticRegression()
classifier_lr1.fit(features_opt , labels_train)
labels_pred_lr1 = classifier_lr1.predict(features_opt_test)


print(confusion_matrix(labels_test,labels_pred_lr1))  
Score_lr1 = accuracy_score(labels_test, labels_pred_lr1)

"""KNN"""
classifier_knn1 = KNeighborsClassifier(n_neighbors = 5, p = 2) 
classifier_knn1.fit(features_opt, labels_train)

probability = classifier_knn1.predict_proba(features_opt_test)

labels_pred_knn1 = classifier_knn1.predict(features_opt_test)

print(confusion_matrix(labels_test, labels_pred_knn1))
Score_knn1 = accuracy_score(labels_test, labels_pred_knn1)


"""BARCHART"""
score = [Score_dtc ,Score_dtc1 , Score_rfc , Score_rfc1 , Score_lr , Score_lr1 ,   Score_knn , Score_knn1]  
nam = ['Score_dtc' ,'Score_dtc1' , 'Score_rfc' , 'Score_rfc1' , 'Score_lr' , 'Score_lr1' ,   'Score_knn' , 'Score_knn1']  

plt.figure(figsize=[8,8])
plt.grid()
plt.bar(nam ,score)
plt.xticks(nam,rotation = 90 , fontsize = 11)
plt.title("Comparision of score" ,fontsize=14)
plt.ylabel("Accuracy" , fontsize = 11)

plt.show()
























