from django.urls import path
from .views import Register


urlpatterns = [
    path('Register/', Register.as_view(), name='user_register_api'),
]