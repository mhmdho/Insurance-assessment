from django.urls import path
from .views import RegisterView, UserProfileView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_register_api'),
    path('profile/', UserProfileView.as_view(), name='user_profile_api'),
]