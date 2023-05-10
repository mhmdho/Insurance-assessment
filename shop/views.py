from django.shortcuts import render
from .serializers import ShopListSerializer, ShopCreateSerializer
from rest_framework import generics
from .models import Shop
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

# Create your views here.


class ShopListView(generics.ListAPIView):
  queryset = Shop.objects.filter(is_confirmed=True)
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
  serializer_class = ShopCreateSerializer
  queryset = Shop.objects.all()

  def get_queryset(self):
      queryset = super().get_queryset()
      return queryset.filter(user=self.request.user, id=self.kwargs['pk'])
