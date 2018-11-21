from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import movie
from . serializers import movieSerializer
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
    movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:16]

    dataframe = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
    dataframeSorted = dataframe.sort_values(['similarity'], ascending=False)[:16]
    return dataframeSorted.index.values

class movieList(generics.RetrieveUpdateDestroyAPIView):
    queryset = movie.objects.all()
    serializer_class = movieSerializer

    def get(self, request):
        return Response("To get list of movies, please POST with the movie name in the data.")

    def post(self, request):
        serializer = movieSerializer(movie)
        data = serializer.data
        movieValue = request.body
        print(movieValue)
        movieValue = str(movieValue)
        movieValue=movieValue[2:-1]
        data['movielist'] = findMovieMatches(movieValue)
        return Response(data)
