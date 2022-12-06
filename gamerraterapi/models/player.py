'''Player/User Class'''
from django.db import models

class Player(models.Model):
    '''Player/User Class'''
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    