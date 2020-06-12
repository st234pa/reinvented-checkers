""" API requests and responses. """
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import Checkerboard, Game, SinglePlayerGame
from . import serializers


class UserCreate(APIView):
    """  Creates the user. """
    permission_classes = (AllowAny,)

    def post(self, request, _='json'):
        """ Creates response with token based on create user POST request. """
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateSinglePlayerGame(APIView):
    """ Create a single player game. """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        board = Checkerboard.create()
        board.save()
        game = Game.create(board=board, name=request.data['name'])
        game.save()
        single_player_game = SinglePlayerGame.create(
            user=request.user,
            user_color=request.data['user_color'],
            game=game
        )
        single_player_game.save()
        serializer = serializers.SinglePlayerGameSerializer(single_player_game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetSinglePlayerGames(APIView):
    """ Get the current user's single player games. """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """ Returns a list of the user's single player games in reverse chronological order. """
        # user_id = request.user.id
        query_set_list = list(SinglePlayerGame.objects.filter(
            user_id__exact=request.user.id).order_by('-game__created_at', 'game__name'))
        serialized_data = [serializers.SinglePlayerGameSerializer(
            game).data for game in query_set_list]
        return Response(serialized_data, status=status.HTTP_200_OK)


class GameDelete(APIView):
    """ Delete a single player game. """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """ Delete the single player game with the given key. """
        game = Checkerboard.objects.filter(pk=request.data['id'])
        game.delete()
        return Response(status=status.HTTP_200_OK)
