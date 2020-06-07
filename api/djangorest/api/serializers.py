""" Serializers """

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import SinglePlayerGame, Checkerboard


class CheckerboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkerboard
        fields = (
            'current_turn',
            'board',
        )



class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=32,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=6, max_length=100,
                                     write_only=True)

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password')


class SinglePlayerGameSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    board = CheckerboardSerializer(many=False)
    user = UserSerializer(many=False)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = SinglePlayerGame
        fields = (
            'name',
            'board',
            'user',
            'user_color',
            'game_status'
        )
