# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:45:46 2021

@author: vidhya
"""

from numpy import random, array

def create_cluster_data(N, k):
    random.seed(10)
    points_per_cluster = float(N) / k
    X = []
    for i in range(k):
        income_centroid = random.uniform(20000.0, 200000.0)
        age_centroid = random.uniform(20.0, 70.0)
        for j in range(int(points_per_cluster)):
            X.append([random.normal(income_centroid, 10000.0), 
                      random.normal(age_centroid, 2.0)])
    X = array(X)
    return X
    

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

data = create_cluster_data(1000, 5)
x = (scale(data))

print('data is : ', x)

model = KMeans(n_clusters=5)
model = model.fit(x)
print(model.labels_)

plt.scatter(x[:,0], x[:,1], c=model.labels_.astype(float))
plt.show()
