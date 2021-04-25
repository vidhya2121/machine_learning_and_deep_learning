# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:55:03 2021

@author: vidhya
"""

import numpy as np
import matplotlib.pyplot as plt

income = np.random.normal(100, 20, 10000)
plt.hist(income, 50)
plt.show()

print('standard deviation : ', income.std())
print('variance : ' , income.var())


