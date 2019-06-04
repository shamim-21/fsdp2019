# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:09:52 2019

@author: Sammu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("tshirts.csv")
features = df.iloc[:,[1,2]].values
plt.scatter(features[:,0], features[:,1])
plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++' , random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'black', label = 'Cluster 1')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('T-shirt')
plt.xlabel('height')
plt.ylabel('weight')
plt.legend()
plt.show()

 