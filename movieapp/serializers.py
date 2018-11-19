from rest_framework import serializers
from . models import movie

class movieSerializer(serializers.ModelSerializer):

    class Meta:
        model = movie
        fields=("moviename", "movie_id", "movieMatches")
