import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from crud.models import CategoriesOfProducts


# class CategoriesModel:

#     def __init__(self, name, seq):
#         self.name = name
#         self.seq = seq

class CategoriesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    seq = serializers.IntegerField()

    def create(self, validated_data):
        return CategoriesOfProducts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.seq = validated_data.get('seq', instance.seq)
        instance.save()
        return instance
    


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