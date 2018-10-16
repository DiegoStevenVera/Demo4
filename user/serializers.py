from rest_framework import serializers
from rest_framework.compat import authenticate
from rest_framework.relations import PrimaryKeyRelatedField

from user.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'DNI', 'name', 'last_name', 'email', 'password'
        )


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id', 'name', 'duration', 'description', 'date', 'photo'
        )


class User_has_MovieSerializerCreated(serializers.ModelSerializer):
    class Meta:
        model = User_has_Movie
        fields = (
            'id', 'User', 'Movie', 'price', 'date', 'time', 'place', 'room_cinema'
        )


class User_has_MovieRUD(serializers.ModelSerializer):
    User = UserSerializer()
    Movie = MovieSerializer()

    class Meta:
        model = User_has_Movie
        fields = (
            'id', 'User', 'Movie', 'price', 'date', 'time', 'place', 'room_cinema'
        )
