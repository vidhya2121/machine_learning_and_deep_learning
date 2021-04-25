# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:48:26 2021

@author: vidhya
"""

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(27000, 15000, 10000)
incomes = np.append(incomes, [100000000])
incomes = np.append(incomes, [1])

plt.hist(incomes, 50)
plt.show()

print('with outliers : mean is :', incomes.mean())

def remove_outliers(data):
    median = np.median(data)
    std_dev = np.std(data)
    filtered = [e for e in data if (median - 2 * std_dev 
                                    < e < median + 2 * std_dev )]
    return filtered

filtered = remove_outliers(incomes)

plt.hist(filtered, 50)
plt.show()

print('mean after removing outliers : ', np.mean(filtered))