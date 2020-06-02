"""
Database models.
"""
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.


class Checkerboard(models.Model):
    """ Checkerboard model. """
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField()
    rows = models.IntegerField()
    columns = models.IntegerField()
    owner = models.ForeignKey(
        'auth.User',
        related_name='bucketlists',
        on_delete=models.CASCADE
    )
    # empty space: ""
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
        return self.name


# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
