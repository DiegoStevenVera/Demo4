from rest_framework import serializers
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


class User_has_MovieSerializer(serializers.ModelSerializer):
    User = UserSerializer(read_only=True)
    Movie = MovieSerializer(read_only=True)

    class Meta:
        model = User_has_Movie
        fields = (
            'id', 'User', 'Movie', 'price', 'date'
        )
