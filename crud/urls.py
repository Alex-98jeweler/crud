from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product-categories', CategoriesViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls))
    # path('product-categories', CategoriesViewSet.as_view({'get':'list', 'post': 'create'})),
    # path('product-categories/<int:pk>', CategoriesViewSet.as_view({'put': 'update', 'delete': 'destroy'}))
]