from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import movie
from . serializers import movieSerializer

class movieList(generics.ListCreateAPIView):
    queryset = movie.objects.all()
    serializer_class = movieSerializer
    # def get(self, request):
    #     movies1=movie.objects.all()
    #     serializer=movieSerializer(movies1, many=True)
    #     return Response(serializer.data)
    #
    # def post(self):
    #     pass

class movieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = movie.objects.all()
    serializer_class = movieSerializer
    # def get(self, request, pk, format=None):
    #     return self.get_object(pk)
    # queryset = movie.objects.all()
    # serializer = movieSerializer
