from django.db import models
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

class movie(models.Model):
    # moviename=models.CharField(max_length=30)
    # movie_id=models.AutoField(primary_key=True)
    # release_date=models.CharField(max_length=20)
    # imdb_link=models.CharField(max_length=100)
    # movieMatches = findMovieMatches('Toy Story (1995)')

    def __str__(self):
        return self.moviename
