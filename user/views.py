from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from user.models import CustomUser
from .serializers import RegisterSerializer, UserProfileSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from django.shortcuts import get_object_or_404

# Create your views here.


class RegisterView(generics.CreateAPIView):
    """
    Takes a set of informations and register user.
    """
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return Response({"Success": "Your registration was successful"}, status=status.HTTP_201_CREATED)


class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    Shows and update the user profile.
    """
    http_method_names = ['put', 'get']
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_object(self):
        return get_object_or_404(CustomUser, id=self.request.user.id)
