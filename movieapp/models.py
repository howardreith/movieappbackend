from django.db import models
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import pandas as pd
import numpy as np

def findMovieMatches(title):
    movieTitle = title

    rating_columns = ['user_id', 'movie_id', 'rating']
    ratings = pd.read_csv('movieapp/u.data', sep='\t', names=rating_columns, usecols=range(3), encoding='ISO-8859-1')

    movie_columns = ['movie_id', 'title']
    movies = pd.read_csv('movieapp/u.item', sep='|', names=movie_columns, usecols=range(2), encoding="ISO-8859-1")

    ratings = pd.merge(movies, ratings)

    movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

    starWarsRatings = movieRatings[movieTitle]

    similarMovies = movieRatings.corrwith(starWarsRatings)
    similarMovies = similarMovies.dropna()
    similarMovies.sort_values(ascending=False)

    movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})

    popularMovies = movieStats['rating']['size'] >= 100
    movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]

    dataframe = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
    dataframeSorted = dataframe.sort_values(['similarity'], ascending=False)[:15]
    return dataframeSorted.index.values

class movie(models.Model):
    moviename=models.CharField(max_length=30)
    movie_id=models.AutoField(primary_key=True)
    # release_date=models.CharField(max_length=20)
    # imdb_link=models.CharField(max_length=100)
    movieMatches = findMovieMatches('Toy Story (1995)')

    def __str__(self):
        return self.moviename
