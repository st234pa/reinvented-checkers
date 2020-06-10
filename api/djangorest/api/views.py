""" API requests and responses. """
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import Checkerboard, SinglePlayerGame
from . import serializers


class SampleView(APIView):
    """ Placeholder protected api endpoint. """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """ Protected get request handler. """
        user = request.user
        content = {'message': 'Hello, ' + user.username + '!'}
        return Response(content, status=HTTP_200_OK)


class UserCreate(APIView):
    """  Creates the user. """
    permission_classes = (AllowAny,)

    def post(self, request, _='json'):
        """ Creates response with token based on create user POST request. """
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateSinglePlayerGame(APIView):
    """ Create a single player game. """

    def post(self, request):
        board = Checkerboard.create()
        board.save()
        game = SinglePlayerGame.create(
            name=request.data['name'],
            user=request.user,
            user_color=request.data['user_color'],
            board=board
        )
        game.save()
        serializer = serializers.SinglePlayerGameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetSinglePlayerGames(APIView):
    """ Get the current user's single player games. """

    def get(self, request):
        """ Returns a list of the user's single player games in reverse chronological order. """
        # user_id = request.user.id
        query_set_list = list(SinglePlayerGame.objects.filter(
            user_id__exact=request.user.id).order_by('-created_at', 'name'))
        serialized_data = [serializers.SinglePlayerGameSerializer(
            game).data for game in query_set_list]
        return Response(serialized_data, status=HTTP_200_OK)


class Login(APIView):
    """ User login. """
    permission_classes = (AllowAny,)

    def post(self, request):
        """ Returns a token or an error based on login POST request. """
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=HTTP_200_OK)


class Logout(APIView):
    """ User logout. """

    def get(self, request):
        """ Delete the token to force a login. """
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
