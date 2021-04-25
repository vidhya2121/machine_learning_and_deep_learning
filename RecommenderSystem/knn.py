# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:52:05 2021

@author: vidhya
"""
import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3))
print(ratings.head())

import numpy as np

movie_properties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})
print(movie_properties.head())

movie_num_ratings = pd.DataFrame(movie_properties['rating']['size'])
print(movie_num_ratings.head())
movie_normalized_num_ratings = movie_num_ratings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
print(movie_normalized_num_ratings.head())

movie_dict = {}
with open(r'ml-100k/u.item') as f:
    temp = ''
    for line in f:
        fields = line.rstrip('\n').split('|')
        movie_id= int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movie_dict[movie_id] = (name, np.array(list(genres)), movie_normalized_num_ratings.loc[movie_id].get('size'), movie_properties.loc[movie_id].rating.get('mean'))
        
print(movie_dict[2])
print(movie_dict[4])

from scipy import spatial

def compute_distance(a, b):
    genresA= a[1]
    genresB = b[1]
    genre_dist = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularity_dist = abs(popularityA - popularityB)
    return genre_dist + popularity_dist

print(compute_distance(movie_dict[2], movie_dict[4]))

import operator

def get_neighbours(movie_id, k):
    distances = []
    for movie in movie_dict:
        if (movie != movie_id):
            dist = compute_distance(movie_dict[movie_id], movie_dict[movie])
            distances.append((movie, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbours = []
    for x in range(k):
        neighbours.append(distances[x][0])
        
    return neighbours

print(get_neighbours(1,10))

k = 10
avg_rating = 0
neigh = get_neighbours(1, k)


for n in neigh:
    avg_rating += movie_dict[n][3]
    print(movie_dict[n][0], " ", movie_dict[n][3])
    
avg_rating /= k
print(avg_rating)

print(movie_dict[1])