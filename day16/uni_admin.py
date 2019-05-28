# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:38:49 2019

@author: Sammu
"""

#import pandas as pd
#import numpy as np
#
#dataset = pd.read_csv('University_data.csv') 
# 
#features = dataset.iloc[:, :6].values  
#labels = dataset.iloc[:, 6].values
#
#from sklearn.linear_model import LinearRegression  
#regressor = LinearRegression()  
#regressor.fit(features, labels) 
#
#x=[]
#x=np.array(x)
#x=x.reshape(1,1)
#
#y=regressor.predict(x)
#print (y)
import numpy as np
import pandas as pd
dataset = pd.read_csv('University_data.csv')
temp = dataset.values
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)


#Pred = regressor.predict(features_test)
#print (pd.DataFrame(Pred, labels_test))

#x = [0,0,0,0,309,5,5,9,1]
#x = np.array(x)
#x=x.reshape(1, 9)
#print(regressor.predict(x))


le = labelencoder.transform(['Cabrini'])
ohe = onehotencoder.transform(le.reshape(1,1)).toarray()
x = [ohe[0][1],ohe[0][2],ohe[0][3],ohe[0][4],309,5,5,9,1]
x = np.array(x)
x=x.reshape(1, 9)
print(regressor.predict(x))

