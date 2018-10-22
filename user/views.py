from rest_framework import generics, status
from .models import *
from .serializers import *
from rest_framework import generics, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


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


class User_has_MovieListView(generics.ListAPIView):
    queryset = User_has_Movie.objects.all()
    serializer_class = User_has_MovieSerializerList


class User_has_MovieCreate(generics.CreateAPIView):
    queryset = User_has_Movie.objects.all()
    serializer_class = User_has_MovieSerializerCreated

class User_has_MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_has_Movie.objects.all()
    serializer_class = User_has_MovieRUD


class SaleUserView(generics.ListAPIView):
    serializer_class = User_has_MovieRUD

    def get_user_sale(self):
        try:
            user = User.objects.get(DNI=self.kwargs['pk'])
        except User.DoesNotExist:
            user = None
        return user

    def get_queryset(self):
        try:
            sale = User_has_Movie.objects.filter(User=self.get_user_sale())
        except User_has_Movie.DoesNotExist:
            sale = None
        return sale