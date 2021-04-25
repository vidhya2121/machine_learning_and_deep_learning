# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:53:09 2021

@author: vidhya
"""

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score

np.random.seed(2)

page_speeds = np.random.normal(3.0, 1.0, 1000)
purchase_amount = np.random.normal(50.0, 10.0, 1000) / page_speeds

scatter(page_speeds, purchase_amount)

x = np.array(page_speeds)
y = np.array(purchase_amount)

p4 = np.poly1d(np.polyfit(x,y,4))

xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p4(xp))
plt.show()

r2 = r2_score(y, p4(x))
print(r2)