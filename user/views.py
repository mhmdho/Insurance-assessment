from django.shortcuts import render
from rest_framework import generics
from user.models import CustomUser
from .serializers import RegisterSerializer

# Create your views here.


class Register(generics.CreateAPIView):
    """
    Takes a set of informations and register user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return Response({"Success": "Your registration was successful"}, status=status.HTTP_201_CREATED)
