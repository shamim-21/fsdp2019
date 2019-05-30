# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:01:55 2019

@author: Sammu
"""

#import csv
#with open("Auto_mpg.txt") as file:
#    file1 = csv.reader(file , delimiter=" ")
#    for item in file1:
#        print(item)
import pandas as pd
import numpy as np
df= pd.read_csv("Auto_mpg.txt" , delimiter="\s+", header=None)
df.columns = [ "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]
print(df['car name'][df['mpg']==df['mpg'].max()])

df['horsepower'] = df['horsepower'].replace('?' , np.NAN )
df['horsepower']= df['horsepower'].astype('float64')
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].mean())

features = df.iloc[:,1:-1].values
labels =  df.iloc[:,0].values
df.isnull().any(axis=0)


#from sklearn.preprocessing import LabelEncoder
#le = LabelEncoder()



from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20, random_state=0)  


from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  

Score = regressor.score(features_test , labels_test)
x=[ 8 , 215 , 100 , 2630 , 22.2 , 80, 3]
x = np.array(x)
x=x.reshape(1, -1)
print(regressor.predict(x))

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test)  
Score2 = regressor.score(features_test , labels_test)

x=[ 8 , 215 , 100 , 2630 , 22.2 , 80, 3]
x = np.array(x)
x=x.reshape(1, -1)
print(regressor.predict(x))
