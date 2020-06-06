"""
Database models.
"""
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


# Create your models here.


class Checkerboard(models.Model):
    """ Checkerboard model. """
    # white's turn --> current_turn = 'w'
    # black's turn --> current_turn = 'b'
    current_turn = models.CharField(max_length=1, blank=False)
    # empty space: "_"
    # white: "w"
    # white king: "W"
    # black: "b"
    # black king: "B"
    board = ArrayField(
        ArrayField(
            models.CharField(max_length=1, blank=True),
        ),
    )

    def __str__(self):
        """ Return a human readable representation of the model instance. """
        rep = ""
        for row in self.board:
            for square in row:
                rep += square + " "
            rep += "\n"
        return rep


# class Profile(models.Model):
#     """ User profile model. """
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     boards = models.ManyToManyField(Checkerboard)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     """ When a save event occurs, create a user profile. """
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     """ When a save event occurs, update a user profile. """
#     instance.profile.save()
