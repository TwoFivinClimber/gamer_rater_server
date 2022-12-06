''''Game_Category model'''
from django.db import models
from .category import Category
from .game import Game

class GameCategory(models.Model):
    '''Game category to handel join'''
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
