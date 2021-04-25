# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:53:09 2021

@author: vidhya
"""

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from scipy import stats

page_speeds = np.random.normal(3.0, 1.0, 1000)
purchase_amount = 100 - (page_speeds + np.random.normal(0, 0.1, 1000)) * 3

scatter(page_speeds, purchase_amount)

slope, intercept, r_value, p_value, std_err = stats.linregress(page_speeds, purchase_amount)

r_sq = r_value ** 2

def predict(x):
    return slope * x + intercept

fitline = predict(page_speeds)

plt.scatter(page_speeds, purchase_amount)
plt.plot(page_speeds, fitline)
plt.show()
