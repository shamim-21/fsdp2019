# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:37:40 2019

@author: Sammu
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("bluegills.csv")
features=df.iloc[:,0:1].values
labels=df.iloc[:,1].values
plt.scatter(features,labels)

from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)
lin_reg_1.score(features, labels)
#for accuracy which is between 0 to 1
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_1.predict(features), color = 'blue')
plt.title('linear regression')
plt.xlabel('length')
plt.ylabel('age')
plt.show()


from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree =2)
features_poly = poly_object.fit_transform(features)


lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)
lin_reg_2.score(features_poly,labels)
#y=features_poly.sort()
plt.scatter(features, labels, color = 'red')
x = np.arange(min(features),max(features),0.2).reshape(-1,1)
plt.plot(x, lin_reg_2.predict(poly_object.transform(x)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('length')
plt.ylabel('age')
plt.show()
print (lin_reg_2.predict(poly_object.transform(np.array([5]).reshape(1,1))))


