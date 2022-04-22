from django.test import TestCase
from django.db import transaction, IntegrityError

from .models import *

class TestModel(TestCase):

    def test_transaction(self):
        
        with transaction.atomic:
            try:
                category = CategoriesOfProducts(name="TESTING NAME", seq=100)
                group = GroupsOfProducts(
                                    category_id = category.pk,
                                    title='TESTING TITLE', 
                                    description = "TEST DESCRIPT",
                                    seq = 100,
                                    )
                category.save()
                group.save()
                transaction.commit()
                self.assertEqual(category.pk, group.category_id)
            except IntegrityError:
                transaction.rollback()

        
