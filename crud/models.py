from turtle import mode
from django.db import models
import uuid

from django.forms import BooleanField

# Create your models here.

class CategoriesOfProducts(models.Model):
    name = models.CharField(max_length=100)
    seq = models.IntegerField(unique=True)


class GroupsProducts:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    category_id = models.ForeignKey('CategoriesOfProducts.id')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    seq = models.IntegerField(unique=True)

    
class Products:
    group_id = models.ForeignKey('GroupsOfProduct.id', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    hidden = BooleanField()

