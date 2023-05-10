from django.shortcuts import render
from .serializers import ShopListSerializer
from rest_framework import generics
from .models import Shop
from rest_framework.permissions import AllowAny

# Create your views here.


class ShopListView(generics.ListAPIView):
  queryset = Shop.objects.filter(is_confirmed=True)
  permission_classes = (AllowAny,)
  serializer_class = ShopListSerializer
