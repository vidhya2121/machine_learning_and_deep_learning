# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:45:44 2021

@author: vidhya
"""

import numpy as np
from pylab import *
from sklearn.preprocessing import MinMaxScaler
from sklearn import svm, datasets

def create_cluster_data(N, k):
    np.random.seed(1234)
    points_per_cluster = float(N) / k
    X = []
    y = []
    for i in range(k):
        income_centroid = np.random.uniform(20000.0, 200000.0)
        age_centroid = np.random.uniform(20.0, 70.0)
        for j in range(int(points_per_cluster)):
            X.append([np.random.normal(income_centroid, 10000.0), 
                      np.random.normal(age_centroid, 2.0)])
            y.append(i)
    X = np.array(X)
    y = np.array(y)
    return X, y
     
(X, y) = create_cluster_data(100, 5)

plt.figure(figsize=(8,6))
plt.scatter(X[:,0], X[:,1], c=y.astype(np.float))
plt.show()

scaling = MinMaxScaler(feature_range=(-1,1)).fit(X)
X = scaling.transform(X)

plt.figure(figsize=(8,6))
plt.scatter(X[:,0], X[:,1], c=y.astype(np.float))
plt.show()

C = 1.0
svc = svm.SVC(kernel='linear', C=C).fit(X,y)

print(svc.predict(scaling.transform([[200000, 40]])))
print(svc.predict(scaling.transform([[50000, 65]])))

def plot_predictions(clf):
    xx, yy = np.meshgrid(np.arange(-1, 1, 0.01), np.arange(-1, 1, 0.01))
    npx = xx.ravel()
    npy = yy.ravel()
    
    sample_points = np.c_[npx, npy]
    Z = clf.predict(sample_points)
    
    plt.figure(figsize=(8,6))
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
    plt.scatter(X[:,0], X[:,1], c=y.astype(np.float))
    plt.show()
    
plot_predictions(svc)