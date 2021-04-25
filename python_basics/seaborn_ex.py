# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:50:07 2021

@author: vidhya
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv")

sns.set()

sns.scatterplot(x = '# Gears', y = 'CombMPG', data=df)
plt.show()

sns.lmplot(x = '# Gears', y = 'CombMPG', data=df)
plt.show()

sns.jointplot(x = '# Gears', y = 'CombMPG', data=df)
plt.show()

sns.boxplot(x = '# Gears', y = 'CombMPG', data=df)
plt.show()

sns.swarmplot(x = '# Gears', y = 'CombMPG', data=df)
plt.show()