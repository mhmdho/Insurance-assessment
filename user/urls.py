from django.urls import path
from .views import RegisterView, UserProfileView, MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='user_register_api'),
    path('profile/', UserProfileView.as_view(), name='user_profile_api'),
]
