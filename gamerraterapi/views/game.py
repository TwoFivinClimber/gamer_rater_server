'''View module for handeling requests for games'''

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gamerraterapi.models import Game, GameCategory


class GameView(ViewSet):
    '''Gamerrater game tpye view'''
    
    def retrieve(self, request, pk ):
      
        try:
            game = Game.objects.get(pk=pk)
            '''Replacing snake_case keys with camelCase for response'''
            serializer = GameSerializer(game) 
            serial_game = serializer.data
            serial_game['yearReleased'] = serial_game.pop('year_released')
            serial_game['numberOfPlayers'] = serial_game.pop('number_of_players')
            serial_game['recAge'] = serial_game.pop('rec_age')
            serial_game['playTime'] = serial_game.pop('play_time')
            
            return Response(serial_game)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def list(self, request):
      '''Handels get many requests for games'''
      
      games = Game.objects.all()
      
      serializer = GameSerializer(games, many=True)
      '''Replacing snake_case keys with camelCase for response to FE'''
      game_serialized = serializer.data
      for game in game_serialized:
        game['yearReleased'] = game.pop('year_released')
        game['numberOfPlayers'] = game.pop('number_of_players')
        game['recAge'] = game.pop('rec_age')
        game['playTime'] = game.pop('play_time')
      
      return Response(game_serialized)
    
    def create(self, request):
      '''Handles POST request for games'''
      '''request.data['xxx'] is looking for camelCase keys from FE'''
      
      game = Game.objects.create(
        title = request.data['title'],
        description = request.data['description'],
        designer = request.data['designer'],
        year_released = request.data['yearReleased'],
        number_of_players = request.data['numberOfPlayers'],
        play_time = request.data['playTime'],
        rec_age = request.data['recAge']
      )
      serializer = GameSerializer(game)
      return Response(serializer.data)
      

class GameSerializer(serializers.ModelSerializer):
    '''JSON serializer'''
    class Meta:
      model = Game
      fields = ('id', 'title', 'description', 'designer', 'year_released', 'number_of_players', 'play_time', 'rec_age')
