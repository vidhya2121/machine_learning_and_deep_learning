# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:49:02 2021

@author: vidhya
"""

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from pylab import *
from itertools import cycle

iris = load_iris()

num_samples, num_features = iris.data.shape
print('Number of samples : ', num_samples)
print('NUmber of features : ', num_features)
print('Output names are : ', iris.target_names)

X = iris.data
print('iris data is : \n', X[:5])

pca = PCA(n_components=1, whiten=True).fit(X)

X_pca = pca.transform(X)

print('PCA components are ', pca.components_)

print('variance ratio : ', pca.explained_variance_ratio_)

print('Targets : ', iris.target)

colors = cycle('rgb')
target_ids = range(len(iris.target_names))
pl.figure()
for i, c, label in zip(target_ids, colors, iris.target_names):
    pl.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 0],
               c=c, label=label)
pl.legend()
pl.show()