from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import movie
from . serializers import movieSerializer

class movieList(APIView):
    def get(self, request):
        movies1=movie.objects.all()
        serializer=movieSerializer(movies1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
