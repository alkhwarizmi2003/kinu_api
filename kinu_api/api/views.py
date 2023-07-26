from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets, serializers, generics, views

class TodoView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    http_method_names = ['get', 'post', 'put']
