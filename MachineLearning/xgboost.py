# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:47:13 2021

@author: vidhya
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import xgboost as xgb

from sklearn.metrics import accuracy_score
print(xgb)
iris = load_iris()

num_samples, num_features = iris.data.shape

print('Number of samples: ', num_samples)
print('Number of features: ', num_features)
print('Target names: ', iris.target_names)

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                            test_size=0.2, random_state=0)

print('Train data shape: ', X_train.shape)
print('Train target shape: ', y_train.shape)
print('Test data shape: ', X_test.shape)
print('Test target shape: ', y_test.shape)

train = xgb.DMatrix(X_train, label=y_train)
test = xgb.DMatrix(X_test, label=y_test)

param = {
    'max_depth': 4,
    'eta': 0.3,
    'objective': 'multi:softmax',
    'num_class': 3}
epochs = 10

model = xgb.train(param, train, epochs)
predictions = model.predict(test)

print('predictions are: ', predictions)
print('accuracy is : ', accuracy_score(y_test, predictions))


