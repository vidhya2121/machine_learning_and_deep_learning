# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:45:39 2021

@author: vidhya
"""

import numpy as np
from scipy import stats

A = np.random.normal(25, 5, 10000)
B = np.random.normal(12, 8, 10000)

print('stat of 2 different distribution with different values : ', 
      stats.ttest_ind(A, B))

B = np.random.normal(25, 5, 10000)
print('stat of 2 different distribution with same values : ',
      stats.ttest_ind(A, B))

A = np.random.normal(25, 5, 100000)
B = np.random.normal(25, 5, 100000)

print('stat of 2 different distribution with same values : ',
      stats.ttest_ind(A, B))
print('stat of same distribution', stats.ttest_ind(A, A))