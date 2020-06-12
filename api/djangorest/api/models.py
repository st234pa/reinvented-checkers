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
        """Create a new checkerboard."""
        checkerboard = cls(
            current_turn='w',
            board=[['_' for square in range(8)] for row in range(8)]
        )
        return checkerboard


class Game(models.Model):
    """ Game model. """
    name = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    board = models.OneToOneField(
        Checkerboard, on_delete=models.CASCADE)

    UNFINISHED = 'unfinished'
    R_WON = 'r_won'
    B_WON = 'b_won'
    DRAW = 'draw'

    GAME_STATUSES = [
        (UNFINISHED, 'Unfinished'),
        (R_WON, 'Red won'),
        (B_WON, 'Black won'),
        (DRAW, 'Draw')
    ]

    game_status = models.CharField(choices=GAME_STATUSES, max_length=10)

    @classmethod
    def create(cls, board, name=name):
        """Create a new game."""
        game = cls(
            board=board,
            name=name,
            game_status=Game.UNFINISHED
        )
        return game


class SinglePlayerGame(models.Model):
    """ Single player game model. """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='single_player_games')
    user_color = models.CharField(max_length=1, blank=False)
    game = models.OneToOneField(
        Game, on_delete=models.CASCADE)

    @classmethod
    def create(cls, user, user_color, game):
        """ Create a single player game. """
        single_player_game = cls(
            user=user, user_color=user_color, game=game)
        return single_player_game
