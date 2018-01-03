#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/1/13 19:01
import json

import pandas as pd

path = r'D:\pyworkspace\pydata-book-master\ch02\movielens\users.dat'
path_1 = r'D:\pyworkspace\pydata-book-master\ch02\movielens\ratings.dat'
path_2 = 'D:\pyworkspace\pydata-book-master\ch02\movielens\movies.dat'

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(path, sep='::', header=None, names=unames, engine='python')
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(path_1, sep='::', header=None, names=rnames, engine='python')
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table(path_2, sep='::', header=None, names=mnames, engine='python')

print(users[:5])
print(ratings[:5])
print(movies[:5])

data = pd.merge(pd.merge(ratings, users), movies)
print(data)