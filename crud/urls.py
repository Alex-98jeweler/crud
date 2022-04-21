from django.urls import path

urlpattens = [
    path('/product-categories/'),
    path('/product-groups/'),
    path('/product-groups/<id:uuid>'),
    path('/products/')
]