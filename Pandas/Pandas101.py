# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:49:39 2021

@author: vidhya
"""
import pandas as pd

df = pd.read_csv("PastHires.csv")
# First 10 records
print(df.head(10))
# LAst 5 records
print(df.tail())
# shape of dataframe
print('Shape of data frame is : ' , df.shape)
# size : shape[0] * shape[1]
print('Size of the data frame is ' ,df.size)
print('Number of records : ', len(df))

print('Column names : ', df.columns)

# Extract one column
print(df['Hired'])
print(df['Hired'][5:])
print(df['Hired'][5])

# Extract two columns
print(df[['Hired', 'Years Experience']])
print(df[['Hired', 'Years Experience']][5:])

# sort
print(df.sort_values(['Years Experience']))

# count by groups
print(df['Level of Education'].value_counts())
degree_count = df['Level of Education'].value_counts()
degree_count.plot(kind='bar')

# new data frame from existing
new_df = df[['Previous employers', 'Hired']][5:10]
print(new_df)
prev_emp = new_df['Previous employers'].value_counts()
print(prev_emp)
prev_emp.plot(kind='bar')





