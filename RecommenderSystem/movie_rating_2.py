# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:52:03 2021

@author: vidhya
"""
import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding='ISO-8859-1')

movie_cols = ['movie_id', 'title']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=movie_cols, usecols=range(2), encoding='ISO-8859-1')

ratings = pd.merge(movies, ratings)
print(ratings.head())

user_rating_data = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')
print(user_rating_data.head())

corr_matrix = user_rating_data.corr()
print(corr_matrix.head())

corr_matrix = user_rating_data.corr(method='pearson', min_periods=100)
print(corr_matrix.head())

my_ratings = user_rating_data.loc[0].dropna()
print('my ratings')

sim_candidates = pd.Series()
for i in range(0, len(my_ratings.index)):
    print("Adding sims for ", my_ratings.index[i])
    sims = corr_matrix[my_ratings.index[i]].dropna()
    sims = sims.map(lambda x: x * my_ratings[i])
    sim_candidates = sim_candidates.append(sims)
    
print('---sorting---')
sim_candidates.sort_values(inplace=True, ascending=False)
print(sim_candidates.head(10))

sim_candidates = sim_candidates.groupby(sim_candidates.index).sum()

sim_candidates.sort_values(inplace=True, ascending=False)
print(sim_candidates.head())

filtered_sim = sim_candidates.drop(my_ratings.index)
print(filtered_sim.head(10))