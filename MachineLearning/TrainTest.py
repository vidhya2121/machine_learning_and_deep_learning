# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:47:13 2021

@author: vidhya
"""
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

np.random.seed(2)

page_speeds = np.random.normal(3, 1, 100)
purchase_amount = np.random.normal(50, 30, 100) / page_speeds

scatter(page_speeds, purchase_amount)
plt.show()

train_x = page_speeds[:80]
test_x = page_speeds[80:]

train_y = purchase_amount[:80]
test_y = purchase_amount[80:]

scatter(train_x, train_y)
plt.show()

scatter(test_x, test_y)
plt.show()

print('type of train_x : ', type(train_x))

p4 = np.poly1d(np.polyfit(train_x, train_y, 6))
xp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])
plt.scatter(train_x, train_y)
plt.plot(xp, p4(xp), c='r')
plt.show()

xp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])
plt.scatter(test_x, test_y)
plt.plot(xp, p4(xp), c='r')
plt.show()

from sklearn.metrics import r2_score

r2_test = r2_score(test_y, p4(test_x))
r2_train = r2_score(train_y, p4(train_x))

print("Train r2 score: ", r2_train, " Test r2 score: ", r2_test)