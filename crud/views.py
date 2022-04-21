from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import *
from .serializers import *


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_per'
    max_page_size = 100
    

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = CategoriesOfProducts.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = Pagination

class GroupsViewSet(viewsets.ModelViewSet):
    queryset = GroupsOfProducts.objects.all()
    serializer_class = GroupsSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category_id']

        
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['group_id']
    search_fields = ['name']


# class CalegoriesList(generics.ListCreateAPIView):
#     queryset = CategoriesOfProducts.objects.all()
#     serializer_class = CategoriesSerializer


# class CategoriesApiUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CategoriesOfProducts.objects.all()
#     serializer_class = CategoriesSerializer


#class CategoriesAPIView(APIView):

#     def get(self, request):
#         lst = CategoriesOfProducts.objects.all()
#         return Response({'categories': CategoriesSerializer(lst, many=True).data})

#     def post(self, request):
#         serializer = CategoriesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         return Response({'category': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': "Method PUT not allowed"})

#         try:
#             instance = CategoriesOfProducts.objects.get(pk=pk)
#         except:
#             return Response({'error': "Object does not exists"})

#         serializer = CategoriesSerializer(data=request.data, instance=instance)
#         serializer.is_valid()
#         serializer.save()
#         return Response({'category': serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if not pk:
#             return Response({"error": "Method delete is not allowed"})

#         try:
#             obj = CategoriesOfProducts.objects.get(pk=pk)
#             obj.delete()
#         except:
#             return Response({"error": "Such object does not exits"})

#         return Response({"status": 'success', 'message': f"Object with {str(pk)} has been deleted"})

        

