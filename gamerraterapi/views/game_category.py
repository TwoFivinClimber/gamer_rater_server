'''View module for game_categories will be called along side CRUD of Games'''

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gamerraterapi.models import GameCategory, Game, Category

class GameCategoryView(ViewSet):
    '''Game_Category type views'''
    
    def list(self, request):
      '''Handles GET all requests'''
      
      game_categories = GameCategory.objects.all()
      
      serializer = CategorySerializer(game_categories, many=True)
      '''Replacing snake_case keys with camelCase for response'''
      gc_serialized = serializer.data
      for gc in gc_serialized:
        gc['categoryId'] = gc.pop('category_id')
        gc['gameId'] = gc.pop('game_id')
      return Response(gc_serialized)

    def create(self, request):
      '''handels POST of game_caegory'''
      
      game = Game.objects.get(pk = request.data['gameId'])
      category = Category.objects.get(pk = request.data['categoryId'])
      
      game_category = GameCategory.objects.create(
        category_id = category,
        game_id = game
      )
      serializer = CategorySerializer(game_category)
      '''Replacing snake_case keys with camelCase for response'''
      gc_serialized = serializer.data
      gc_serialized['categoryId'] = gc_serialized.pop('category_id')
      gc_serialized['gameId'] = gc_serialized.pop('game_id') 
      
      return Response(gc_serialized)
      
    
class CategorySerializer(serializers.ModelSerializer):
    '''JSON Serializer'''
    class Meta:
      model = GameCategory
      fields = ('id', 'category_id', 'game_id')
      
      
      
