'''category model'''
from django.db import models

class Category(models.Model):
    '''category class'''
    label = models.CharField(max_length=50)
  