# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:50:07 2021

@author: vidhya
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv")
gear_count = df['# Gears'].value_counts()
gear_count.plot(kind='bar')
plt.show()

sns.set()
print(df.head())

sns.distplot(df['CombMPG'])

df2 = df[['Cylinders', 'CityMPG', 'HwyMPG', 'CombMPG']]
print(df.head())

sns.pairplot(df2, height=2.5)
plt.show()

sns.scatterplot(x = 'Eng Displ', y = 'CombMPG', data=df)
plt.show()

sns.jointplot(x = 'Eng Displ', y = 'CombMPG', data=df)
plt.show()

sns.lmplot(x = 'Eng Displ', y = 'CombMPG', data=df)
plt.show()

sns.set(rc = {'figure.figsize': (15, 5)})
a = sns.boxplot(x = 'Mfr Name', y = 'CombMPG', data=df)
a.set_xticklabels(a.get_xticklabels(), rotation=45)
plt.show()

b = sns.swarmplot(x = 'Mfr Name', y = 'CombMPG', data=df)
a.set_xticklabels(b.get_xticklabels(), rotation=45)
plt.show()

c = sns.countplot(x = 'Mfr Name', data=df)
c.set_xticklabels(c.get_xticklabels(), rotation=45)
plt.show()

df3 = df.pivot_table(index='Cylinders', columns='Eng Displ', values='CombMPG',
                     aggfunc='mean')
sns.heatmap(df3)
plt.show()

