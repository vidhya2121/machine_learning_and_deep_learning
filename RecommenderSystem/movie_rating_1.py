# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:52:04 2021

@author: vidhya
"""

import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding='ISO-8859-1')

movie_cols = ['movie_id', 'title']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=movie_cols, usecols=range(2), encoding='ISO-8859-1')

print(ratings.head())
print(movies.head())

movie_ratings = pd.merge(ratings, movies)
print(movie_ratings.head(-5))

movie_rating_data = movie_ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')
print(movie_rating_data.head())

star_war_ratings = movie_rating_data['Star Wars (1977)']
print(star_war_ratings.head())

similar_movies = movie_rating_data.corrwith(star_war_ratings)
similar_movies = similar_movies.dropna()

df = pd.DataFrame(similar_movies)
print(df.head(10))

print(similar_movies.sort_values(ascending=False))

import numpy as np

movie_stats = movie_ratings.groupby('title').agg({'rating': [np.size, np.mean]})
print(movie_stats.head())

popular_movies = movie_stats['rating']['size'] >= 100
print(popular_movies[:10])
print(movie_stats[popular_movies].sort_values([('rating', 'mean')], ascending=False)[:10])

df2 = movie_stats[popular_movies].join(pd.DataFrame(similar_movies, columns=['similarity']))
print(df2.head())
print(df2.sort_values(['similarity'], ascending=False)[:15])