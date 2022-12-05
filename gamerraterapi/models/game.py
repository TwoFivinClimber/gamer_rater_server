'''Game Class'''
from django.db import models


class Game(models.Model):
    '''Game Class'''
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    designer = models.CharField(max_length=50)
    year_released = models.DateField()
    number_of_players = models.IntegerField()
    play_time = models.IntegerField()
    rec_age = models.IntegerField()
    