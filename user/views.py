from rest_framework import generics
from .models import *
from .serializers import *


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class User_has_MovieListView(generics.ListCreateAPIView):
    queryset = User_has_Movie.objects.all()
    serializer_class = User_has_MovieSerializer


class User_has_MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_has_Movie.objects.all()
    serializer_class = User_has_MovieSerializer
