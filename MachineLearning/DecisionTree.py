# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:45:46 2021

@author: vidhya
"""

import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from IPython.display import Image
from six import StringIO
import matplotlib.pyplot as plt
import pydotplus

input_file = 'PastHires.csv'
df = pd.read_csv(input_file, header=0)

print(df.head())

d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)

d = {'BS':0, 'MS':1, 'PhD':2}
df['Level of Education'] = df['Level of Education'].map(d)

print(df.head())

features = list(df.columns[:6])
print(features)

y = df["Hired"]
print(df["Level of Education"])
X = df[features]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=features)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
plt.show()

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X,y)

# Predict employment of employed 10 year veteran
print(clf.predict([[10, 1, 4, 0, 0, 0]]))

# Predict employment of unemployed 10 year vetern
print(clf.predict([[10, 0, 4, 0, 0, 0]]))