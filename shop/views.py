from django.shortcuts import render
from .serializers import ShopListSerializer, ShopCreateSerializer, ProductListSerializer
from rest_framework import generics
from .models import Shop, Product
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

# Create your views here.


class ShopListView(generics.ListAPIView):
  queryset = Shop.objects.all()
  permission_classes = (AllowAny,)
  serializer_class = ShopListSerializer


class CreateShopView(generics.CreateAPIView):
  permission_classes = (IsAuthenticated,)
  serializer_class = ShopCreateSerializer
  parser_classes = (MultiPartParser, FormParser)

  def perform_create(self, serializer):
      serializer.validated_data['user'] = self.request.user
      serializer.save()


class EditShopView(generics.RetrieveUpdateAPIView):
  permission_classes = (IsAuthenticated,)
  serializer_class = ShopCreateSerializer
  parser_classes = (MultiPartParser, FormParser)
  queryset = Shop.objects.all()

  def get_queryset(self):
      queryset = super().get_queryset()
      return queryset.filter(user=self.request.user, id=self.kwargs['pk'])


class ProductListView(generics.ListAPIView):
  queryset = Product.objects.all()
  permission_classes = (IsAuthenticated,)
  serializer_class = ProductListSerializer

  def get_queryset(self):
      queryset = super().get_queryset()
      return queryset.filter(shop__user=self.request.user, shop_id=self.kwargs['pk'])
