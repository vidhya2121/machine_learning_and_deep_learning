# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:48:26 2021

@author: vidhya
"""

import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                        test_size=0.4, random_state=0)

clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
print('clf score with linear kernel', clf.score(X_test, y_test))
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print('cross_val_score scores for 5 folds : ', scores)
print('mean cross_val_score for linear kernel : ', scores.mean())

clf = svm.SVC(kernel='poly', degree=4, C=1).fit(X_train, y_train)
print('clf score with poly4 kernel : ', clf.score(X_test, y_test))
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print('cross_val_score scores for 5 folds : ', scores)
print('mean cross_val_score for poly4 kernel', scores.mean())