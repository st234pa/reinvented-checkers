""" Database models. """
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


# Create your models here.

class Checkerboard(models.Model):
    """ Board model. """
    # white's turn --> current_turn = 'r'
    # black's turn --> current_turn = 'b'
    current_turn = models.CharField(max_length=1, blank=False)
    # empty space: "_"
    # red: "r"
    # red king: "R"
    # black: "b"
    # black king: "B"
    board = ArrayField(
        ArrayField(
            models.CharField(max_length=1, blank=False),
        ),
    )

    @classmethod
    def create(cls):
        checkerboard = cls(
            current_turn='w',
            board=[['_' for square in range(8)] for row in range(8)]
        )
        return checkerboard


class SinglePlayerGame(models.Model):
    """ Single player game model. """

    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='single_player_games')

    board = models.OneToOneField(
        Checkerboard, on_delete=models.PROTECT, primary_key=True,)

    user_color = models.CharField(max_length=1, blank=False)

    name = models.CharField(max_length=200, blank=False)

    UNFINISHED = 'unfinished'
    USER_WON = 'user_won'
    USER_LOST = 'user_lost'
    DRAW = 'draw'

    GAME_STATUSES = [
        (UNFINISHED, 'Unfinished'),
        (USER_WON, 'You Won'),
        (USER_LOST, 'You Lost'),
        (DRAW, 'Draw')
    ]

    game_status = models.CharField(choices=GAME_STATUSES, max_length=10)

    @classmethod
    def create(cls, user, board, user_color, name):
        single_player_game = cls(
            user=user,
            name=name,
            board=board,
            user_color=user_color,
            game_status=SinglePlayerGame.UNFINISHED
        )
        return single_player_game
