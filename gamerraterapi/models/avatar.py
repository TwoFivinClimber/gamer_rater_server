'''avatar model'''
from django.db import models
from .player import Player

class Avatar(models.Model):
    '''Avatar Image Class'''
    url = models.ImageField(upload_to='images/avatars')
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
  