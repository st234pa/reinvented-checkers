""" Serializers """

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Game, SinglePlayerGame, Checkerboard


class CheckerboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkerboard
        fields = (
            'pk',
            'current_turn',
            'board',
        )


class GameSerializer(serializers.ModelSerializer):
    board = CheckerboardSerializer(many=False)

    class Meta:
        model = Game
        fields = (
            'board',
            'game_status',
            'created_at',
            'updated_at',
            'name',
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

    user = UserSerializer(many=False)
    game = GameSerializer(many=False)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = SinglePlayerGame
        fields = ('user', 'user_color',  'game', )
