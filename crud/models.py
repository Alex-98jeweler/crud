from django.db import models
import uuid


class CategoriesOfProducts(models.Model):
    name = models.CharField(max_length=100)
    seq = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return self.name


class GroupsOfProducts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    category_id = models.ForeignKey(CategoriesOfProducts, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    seq = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return self.title

     
class Products(models.Model):
    group_id = models.ForeignKey(GroupsOfProducts, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    hidden = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

