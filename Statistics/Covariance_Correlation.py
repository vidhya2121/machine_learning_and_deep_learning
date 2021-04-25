# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:55:12 2021

@author: vidhya
"""

import numpy as np
from pylab import *
import matplotlib.pyplot as plt

def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]

def covariance(x,y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    stddev_x = x.std()
    stddev_y = y.std()
    return covariance(x, y) / (stddev_x * stddev_y)

# pageSpeed and purchaseAmount, random, indep of each other
# except very small covar, so no correl
    
page_speed = np.random.normal(3, 1, 1000)
purchase_amount = np.random.normal(50, 10, 1000)

scatter(page_speed, purchase_amount)
plt.show()
print('covariance : ' + str(covariance(page_speed, purchase_amount)))
print('correlation : ' + str(correlation(page_speed, purchase_amount)))
# using numpy
print(np.corrcoef(page_speed, purchase_amount))

# pageSpeed and purchaseAmount, dependent of each other
# except some correl
purchase_amount =  np.random.normal(50, 10, 1000) / page_speed
scatter(page_speed, purchase_amount)
plt.show()
print('covariance : ' + str(covariance(page_speed, purchase_amount)))
print('correlation : ' + str(correlation(page_speed, purchase_amount)))
# using numpy
print(np.corrcoef(page_speed, purchase_amount))

# High covar and correl due to linear dependency
purchase_amount =  100 - page_speed * 3
scatter(page_speed, purchase_amount)
plt.show()
print('covariance : ' + str(covariance(page_speed, purchase_amount)))
print('correlation : ' + str(correlation(page_speed, purchase_amount)))
# using numpy
print(np.corrcoef(page_speed, purchase_amount))

