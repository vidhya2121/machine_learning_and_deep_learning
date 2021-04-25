# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:55:11 2021

@author: vidhya
"""

import numpy as np
from scipy import stats

incomes = np.random.normal(27000, 15000, 10000)
print('mean : ' + str(np.mean(incomes)))
print('median : ' + str(np.median(incomes)))

# outliers
incomes = np.append(incomes, [100000000000000000])
print('mean : ' + str(np.mean(incomes)))
print('median : ' + str(np.median(incomes)))
# median is tolerant to outliers

# mode
age = np.random.randint(18, high=50, size=100)
print(age)

print('mode:', stats.mode(age))


