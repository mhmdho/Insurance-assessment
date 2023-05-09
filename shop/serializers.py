from rest_framework import serializers
from shop.models import Shop


class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', 'type', 'address', 'user', 'is_confirmed')