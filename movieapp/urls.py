# movieapp/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from movieapp import views

urlpatterns = [
    path('movies/', views.movieList.as_view()),
    path('movies/<int:pk>/', views.movieDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
