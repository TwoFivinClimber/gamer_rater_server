'''Rating class'''
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .player import Player
from .game import Game


class Rating(models.Model):
    '''Rating Class'''
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=0, validators=[
                                              MinValueValidator(0),
                                              MaxValueValidator(10)
                                              ])
