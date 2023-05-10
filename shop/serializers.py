from rest_framework import serializers
from shop.models import Shop
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
