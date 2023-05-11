from django.urls import path
from .views import ShopListView, CreateShopView, EditShopView, ProductListView


urlpatterns = [
    path('shoplist/', ShopListView.as_view(), name='shop_list_api'),
    path('createshop/', CreateShopView.as_view(), name='create_shop_api'),
    path('editshop/<int:pk>/', EditShopView.as_view(), name='edit_shop_api'),
    path('<int:pk>/productlist/', ProductListView.as_view(), name='product_list_api'),
  
]
