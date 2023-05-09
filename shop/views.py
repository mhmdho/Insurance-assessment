from django.shortcuts import render
from .serializers import ShopListSerializer
from rest_framework import generics

# Create your views here.


class ShopListView(generics.ListAPIView):
  queryset = Shop.objects.filter(is_confirmed=True)
  serializer_class = ShopListSerializer
