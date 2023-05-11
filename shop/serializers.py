from rest_framework import serializers
from shop.models import Shop, Product
from user.serializers import UserPhoneSerializer


class ShopListSerializer(serializers.ModelSerializer):
    user = UserPhoneSerializer()

    class Meta:
        model = Shop
        fields = ('id', 'name', 'type', 'address', 'user', 'is_confirmed')


class ShopCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'type', 'address')


class ProductListSerializer(serializers.ModelSerializer):
    shop = ShopCreateSerializer()

    class Meta:
        model = Product
        fields = ('id', 'slug', 'name', 'price', 'stock', 'description', 'shop')


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock', 'description')
