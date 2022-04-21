import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import *


# class CategoriesModel:

#     def __init__(self, name, seq):
#         self.name = name
#         self.seq = seq

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesOfProducts
        fields = "__all__"


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupsOfProducts
        fields = "__all__"
  
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
  

# def encode():
#     model = CategoriesModel('Piska', 5)
#     model_sr = CategoriesSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json.decode('utf-8'))

# def decode():
#     stream = io.BytesIO(b'{"name":"piska","seq":5}')
#     data = JSONParser().parse(stream)
#     serializer = CategoriesSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)