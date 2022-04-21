from django.urls import path
from .views import *


urlpatterns = [
    path('product-categories', CategoriesAPIView.as_view()),
    path('product-categories/<int:pk>', CategoriesAPIView.as_view())
]