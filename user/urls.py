from django.urls import path
from .views import RegisterView


urlpatterns = [
    path('Register/', RegisterView.as_view(), name='user_register_api'),
]