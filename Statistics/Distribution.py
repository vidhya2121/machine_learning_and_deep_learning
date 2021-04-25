# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:55:11 2021

@author: vidhya
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm,expon,binom,poisson

# Uniform
values = np.random.uniform(-10, 10, 100000)
plt.hist(values, 50)
plt.show()

# GAussian Normal
x = np.arange(-3, 3, 0.01)
plt.plot(x, norm.pdf(x))
plt.show()


mean = 5
sigma = 2
normal = np.random.normal(mean, sigma, 10000)
plt.hist(normal, 50)
plt.show()

# Exponential
x = np.arange(0, 10, 0.01)
plt.plot(x, expon.pdf(x))
plt.show()

# binomial
n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x, n, p))
plt.show()

# poisson
mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))
plt.show()

