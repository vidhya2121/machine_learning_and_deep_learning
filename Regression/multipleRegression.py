# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:53:09 2021

@author: TeddyBear
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')
df1 = df[['Mileage', 'Price']]
bins = np.arange(0, 50000, 10000)
groups = df1.groupby(pd.cut(df1['Mileage'],bins)).mean()

print(groups.head())
groups['Price'].plot.line()

X = df[['Mileage', 'Cylinder', 'Doors']]
y = df[['Price']]

scale = StandardScaler()
X[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(
    X[['Mileage', 'Cylinder', 'Doors']].values)

print(X.head())

est = sm.OLS(y, X).fit()
print(est.summary())

r = y.groupby(df.Doors).mean()
print(r)

scaled = scale.transform([[45000, 8 , 4]])
print(scaled)

predicted = est.predict(scaled[0])
print(predicted)