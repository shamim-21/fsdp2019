# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:34:58 2019

@author: Sammu
"""
import pandas as pd
import numpy as np

dataset = pd.read_csv('Foodtruck.csv') 
 
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

x=[3.073]
x=np.array(x)
x=x.reshape(1,1)

y=regressor.predict(x)
print (y)
if y<0:
    print("loss")
    

 
#from sklearn.model_selection import train_test_split  
#features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  
#from sklearn.linear_model import LinearRegression  
#regressor = LinearRegression()  
#regressor.fit(features_train, labels_train) 
#labels_pred = regressor.predict(features_test) 


