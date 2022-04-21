from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import *
from rest_framework import routers


categories_router = routers.SimpleRouter()
categories_router.register(r'product-categories', CategoriesViewSet)

groups_router = routers.SimpleRouter()
groups_router.register(r'product-groups', GroupsViewSet)


urlpatterns = [
    path('api/v1/', include(categories_router.urls)),
    path('api/v1/', include(groups_router.urls)),
    path('api/v1/products/', ProductsViewSet.as_view({'get':'list', 'post':'create'})),
    


    # path('product-categories', CategoriesViewSet.as_view({'get':'list', 'post': 'create'})),
    # path('product-categories/<int:pk>', CategoriesViewSet.as_view({'put': 'update', 'delete': 'destroy'}))
]