from django.shortcuts import render
from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework import generics,authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    """"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user, 
       Used for read or update endpoints to represent a single model instance."""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user

