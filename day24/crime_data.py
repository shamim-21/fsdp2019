# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:52:18 2019

@author: Sammu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("crime_data.csv")
#features = df.iloc[:,[0,1]].values
#
#plt.scatter(features[:,0],features[:,1])
#plt.show()

features = df.iloc[:,[1,2,4]].values

#from sklearn.model_selection import train_test_split
#features_train , features_test = train_test_split(features , test_size = 0.2 , random_state =0)

#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#
#features_train = sc.fit_transform(features_train)
#features_test = sc.transform(features_test)

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)
#features_train = pca.fit_transform(features_train)
#features_test = pca.transform(features_test)
explained_variance = pca.explained_variance_ratio_

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3 , init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Crime rate')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()
