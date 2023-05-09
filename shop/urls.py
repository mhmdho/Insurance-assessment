from django.urls import path
from .views import ShopListView


urlpatterns = [
    path('shoplist/', ShopListView.as_view(), name='shop_list_api'),
]
