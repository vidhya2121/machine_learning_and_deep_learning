# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:50:09 2021

@author: vidhya
"""

# very basic python syntax 

print("hello")

# even or odd
list_of_numbers = [1, 2, 3, 4, 5, 6, 7,]

for num in list_of_numbers:
    if (num % 2 == 0):
        print(num, ' : is even')
    else:
        print(num, " : is odd")
        
print("All done")

# arrays, list
import numpy as np

A = np.random.normal(25, 5, 10)
print(A)

x = [1, 2, 3, 4, 5, 6]
print(x[:3])
print(x[3:])
print(x[-2:])
x.extend([7,8])
print(x)
x.append(9)
print(x)
y = [10, 11, 12]
list_of_lists = [x, y]
print(list_of_lists)
print(y[1])
print(list_of_lists[0][1])
z = [3, 2, 1]
z.sort()
print(z)
z.sort(reverse=True)
print(z)

# Tuples are immutable
xx = (1,2,3)
print(xx)
yy = (4,5,6)
print(yy[1])
list_of_tuples = [xx, yy]
print(list_of_tuples)
(age, incomes) = "32,60000".split(',')
print('age= ', age, " income ", incomes)

# dictionary
captains = {}
captains['Enterprise'] = "Kirk"
captains['Enterprise D'] = "Picard"
captains['Voyager'] = "JAneway"
print(captains)
print(captains['Voyager'])
print(captains.get('Voyager'))
print(captains.get('NX-01'))

for ship in captains:
    print(ship, " " , captains[ship])














