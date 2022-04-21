import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import *
from .logics import set_seq, get_max


class Base(serializers.ModelSerializer):
    def __init__(self, instance=None, data=..., **kwargs):
        kwargs['partial'] = True
        super(Base, self).__init__(instance, data, **kwargs)


class CategoriesGroupBase(Base):

    def create(self, validated_data):
        try:
            validated_data['seq']
        except KeyError:
            validated_data['seq'] = set_seq(self.Meta.model)
        if validated_data['seq'] <= get_max(self.Meta.model):
            validated_data['seq'] = set_seq(self.Meta.model)
        return super(CategoriesGroupBase, self).create(validated_data)


class CategoriesSerializer(CategoriesGroupBase):

    class Meta:
        model = CategoriesOfProducts
        fields = "__all__"


class GroupsSerializer(CategoriesGroupBase):

    class Meta:
        model = GroupsOfProducts
        fields = "__all__"


class ProductsSerializer(Base):

    class Meta:
        model = Products
        fields = "__all__"
