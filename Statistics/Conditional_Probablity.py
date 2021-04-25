# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:55:12 2021

@author: vidhya
"""

from numpy import random

random.seed(0)

# Total number of number of people in a age group & purchases done by various age group
totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}

total_purchases = 0

for _ in range(100000):
    age_decade = random.choice([20, 30, 40, 50, 60, 70])
    # the data is created such that purchases increases with age
    purchase_prob = age_decade / 100
    totals[age_decade] += 1
    if(random.random() < purchase_prob):
        total_purchases += 1
        purchases[age_decade] += 1
        
print(totals)
print(purchases)
print(total_purchases)

# P(E|F)  P(Purchase|age=30)

PEF = purchases[30] / totals[30]
print('P(Purchase|age=30) : ' + str(PEF))

PF = totals[30] / 100000
print('P(age=30) : ' + str(PF))

PE = total_purchases / 100000
print('P(Purchases) : ' + str(PE))

# P(E,F)
print('P(E,F) : ' + str(purchases[30]/100000))

# only dep, then P(E,F) is not equal to P(E)P(F)
print('P(E)P(F) : ' + str(PE * PF))

print('P(E,F)/P(F) : ' + str(purchases[30]/(100000 * PF)))