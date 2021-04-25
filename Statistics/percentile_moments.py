# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:55:10 2021

@author: vidhya
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

income = np.random.normal(60000, 50, 1000000)
plt.hist(income, 50)
plt.show()

print("50th percentile", np.percentile(income, 50))
print("9th percentile", np.percentile(income, 90))


print('mean', np.mean(income))
print('variance', np.var(income))
print('skew', sp.skew(income))
print('kurtosis', sp.kurtosis(income))