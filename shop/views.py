from django.shortcuts import render
from .serializers import ShopListSerializer, ShopCreateSerializer, ProductListSerializer, ProductCreateSerializer
from rest_framework import generics
from .models import Shop, Product
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

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
  pagination_class = PageNumberPagination

  def get_queryset(self):
      queryset = super().get_queryset()
      return queryset.filter(shop__user=self.request.user, shop_id=self.kwargs['pk'])


class CreateProductView(generics.CreateAPIView):
  permission_classes = (IsAuthenticated,)
  serializer_class = ProductCreateSerializer
  parser_classes = (MultiPartParser, FormParser)

  def perform_create(self, serializer):
      shop = Shop.objects.filter(id=self.kwargs['pk']).first()
      if shop.user == self.request.user:
        serializer.validated_data['shop'] = shop
        serializer.save()
        return Response({'success': 'Product added successfully.'},
                status=status.HTTP_201_CREATED)
      else:
        return Response({'error': 'You do not have permission to add a product to this shop.'},
                        status=status.HTTP_401_UNAUTHORIZED)


class EditProductView(generics.RetrieveUpdateAPIView):
  lookup_field = 'slug'
  permission_classes = (IsAuthenticated,)
  serializer_class = ProductCreateSerializer
  parser_classes = (MultiPartParser, FormParser)
  queryset = Product.objects.all()

  def get_queryset(self):
      queryset = super().get_queryset()
      return queryset.filter(shop__user=self.request.user, slug=self.kwargs['slug'])
