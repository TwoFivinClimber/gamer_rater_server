'''category module for get only'''

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gamerraterapi.models import Category

class CategoryView(ViewSet):
    '''Category type views'''
    
    def list(self, request):
      '''Handles GET all requests'''
      
      categories = Category.objects.all()
      
      serializer = CategorySerializer(categories, many=True)
      '''formats response for react-select'''
      cat_format = serializer.data
      for cat in cat_format:
        cat['value'] = cat.pop('id')
      return Response(cat_format)

class CategorySerializer(serializers.ModelSerializer):
    '''JSON Serializer'''
    class Meta:
      model = Category
      fields = ('id', 'label')
