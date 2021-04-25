# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:50:10 2021

@author: vidhya
"""
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# Plot a pdf
x = np.arange(-3, 3, 0.01)
plt.plot(x, norm.pdf(x))
plt.show()

# multiple plots
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1, 0.5))
plt.show()

# save a plot
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1, 0.5))
plt.savefig('Myplot.png', format='png')

axes = plt.axes()
axes.set_xlim([-5,5])
axes.set_ylim([0,1])
axes.set_xticks([-5,-4,-3,-2,-1,1,2,3,4,5])
axes.set_yticks([0.1,0.2,0.3,0.4,0.6,0.7,0.8,0.9,1])
axes.grid()
plt.xlabel('values')
plt.ylabel('Probablity')
plt.plot(x, norm.pdf(x), 'g-', label='AA')
plt.plot(x, norm.pdf(x, 1, 0.5), 'r-.', label='BB')
legend = axes.legend()
axes.legend(loc='upper right')
plt.show()

values = [12, 55, 4 ,32, 14]
colors = ['r', 'g', 'b', 'c', 'y']
# show a particular block of pie-chart projected
explode = [0, 0, 0.2, 0, 0]
labels = ['India', 'US', 'Russia', 'China', 'Europe']
plt.pie(values, labels=labels, explode=explode, colors=colors)
plt.title('Student locations')
plt.show()

plt.bar(labels, values, color=colors)
plt.show()

plt.scatter(np.random.randn(500), np.random.randn(500))
plt.show()

incomes = np.random.normal(27000, 15000, 1000)
plt.hist(incomes, 50)
plt.show()

uniform_skew = np.random.rand(100) * 100 - 40
high_outlier = np.random.rand(10) * 50 + 100
low_outlier = np.random.rand(10) * -50 - 100
data_box = np.concatenate((uniform_skew, high_outlier, low_outlier))
plt.boxplot(data_box)
plt.show()


